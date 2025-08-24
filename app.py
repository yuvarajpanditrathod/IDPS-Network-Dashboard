from flask import Flask, render_template, request, jsonify, make_response
import psutil
import random
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objs as go
import plotly
import json
from flask_pymongo import PyMongo
from config import Config
import subprocess
import re
import socket
import threading

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
logs_collection = mongo.db.network_logs

mitigated_ips = set()
connected_devices_cache = []
last_scan_time = datetime.min

import torch
import joblib
import pickle
import tensorflow as tf

def load_models():
    try:
        torch.load('models/ensemble_voting_model.pkl', map_location=torch.device('cpu'))
        torch.load('models/isolation_forest_model.pkl', map_location=torch.device('cpu'))
        torch.load('models/xgboost_attack_classifier_weighted.pkl', map_location=torch.device('cpu'))

        joblib.load('models/anomaly_scaler.pkl')
        joblib.load('models/attack_feature_scaler.pkl')
        with open('models/attack_label_encoder.pkl', 'rb') as f:
            pickle.load(f)
        with open('models/label_encoder.pkl', 'rb') as f:
            pickle.load(f)

        tf.keras.models.load_model('autoencoder_model.h5')
        tf.keras.models.load_model('cnn_lstm_model.keras')

        print("All ML models loaded successfully.")

    except Exception as e:
        print(f"Model loading failed: {e}")

def get_connected_devices():
    """Optimized device scanning with caching and threading"""
    global connected_devices_cache, last_scan_time
    
    if (datetime.now() - last_scan_time).total_seconds() < 30 and connected_devices_cache:
        return connected_devices_cache
    
    def scan_devices():
        global connected_devices_cache, last_scan_time
        devices = []
        
        try:
            if subprocess.os.name == 'nt':
                arp_output = subprocess.check_output(["arp", "-a"], timeout=5).decode('ascii', errors='ignore')
                pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9-]{17}|incomplete)"
            else:
                arp_output = subprocess.check_output(["arp", "-a"], timeout=5).decode('utf-8', errors='ignore')
                pattern = r"(\d+\.\d+\.\d+\.\d+)\s+[^\s]+\s+([a-fA-F0-9:]{17}|incomplete)"
            
            matches = re.findall(pattern, arp_output)
            
            for ip, mac in matches:
                if mac.lower() == 'incomplete':
                    continue
                devices.append({
                    'ip': ip,
                    'mac': mac if mac else 'unknown',
                    'hostname': None,
                    'status': 'online',
                    'last_seen': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            
            def resolve_hostname(device):
                try:
                    device['hostname'] = socket.gethostbyaddr(device['ip'])[0]
                except (socket.herror, socket.gaierror):
                    device['hostname'] = f"host-{device['mac'].replace(':', '')[-5:]}" if device['mac'] != 'unknown' else f"host-{device['ip'].split('.')[-1]}"
                return device
            
            threads = []
            for device in devices:
                t = threading.Thread(target=lambda d: resolve_hostname(d), args=(device,))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join(timeout=1)
            unique_devices = []
            seen_ips = set()
            for device in devices:
                if device['ip'] not in seen_ips:
                    seen_ips.add(device['ip'])
                    unique_devices.append(device)
            
            connected_devices_cache = unique_devices
            last_scan_time = datetime.now()
            
        except Exception as e:
            print(f"Network scan error: {e}")
            return connected_devices_cache
    
    scan_thread = threading.Thread(target=scan_devices)
    scan_thread.start()
    
    return connected_devices_cache

def generate_and_store_logs():
    """Optimized log generation with bulk inserts and realistic SOC-style fields"""
    new_logs = []
    attack_types = ['DDoS', 'DoS', 'Brute Force', 'Port Scan', 'SQL Injection', 'Web Attacks', 'XSS']
    protocols = ['TCP', 'UDP', 'ICMP', 'HTTP', 'HTTPS']
    threat_sources = ['AlienVault', 'Spamhaus', 'AbuseIPDB', 'Cisco Talos', 'FireEye']
    country_codes = ['China', 'Russia', 'India', 'US', 'Brazil', 'Germany', 'DE', 'NG']

    def generate_public_ip():
        first_octet = random.choice([i for i in range(1, 256) if i not in [10, 127, 172, 192]])
        return f"{first_octet}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for _ in range(10):
        src_ip = generate_public_ip()
        attack_type = random.choice(attack_types)
        new_logs.append({
            'timestamp': timestamp,
            'src_ip': src_ip,
            'dst_ip': '	10.1.23.194',
            'action': 'DETECT',
            'protocol': random.choice(protocols),
            'port': random.randint(1, 65535),
            'size': random.randint(1024, 4096),
            'alert': 'ALERT',
            'attack_type': attack_type,
            'threat_source': random.choice(threat_sources),
            'signature': f"{attack_type}-SIG-{random.randint(1000,9999)}",
            'geo': random.choice(country_codes)
        })

    # Bulk insert for performance
    if new_logs:            
        try:
            logs_collection.insert_many(new_logs)
        except Exception as e:
            print(f"Error inserting logs: {e}")

    logs = list(logs_collection.find({}, {'_id': False}).sort('timestamp', -1).limit(100))
    return logs

def detect_malicious_ips(logs):
    """Detect potentially malicious IPs from logs"""
    malicious_ips = []
    attack_counts = {}
    for log in logs:
        if log['src_ip'] in mitigated_ips:
            continue
        if not any(ip['ip'] == log['src_ip'] for ip in malicious_ips):
            malicious_ips.append({
                'ip': log['src_ip'],
                'threat_level': 'high',
                'first_detected': log['timestamp'],
                'attack_type': log['attack_type']   
            })
        attack_counts[log['attack_type']] = attack_counts.get(log['attack_type'], 0) + 1
    return malicious_ips, attack_counts

def create_interactive_attack_chart(attack_stats):
    """Create Plotly pie chart of attack types"""
    if not attack_stats:
        return ""
    labels = list(attack_stats.keys())
    values = list(attack_stats.values())
    pulls = [round(random.uniform(0.05, 0.15), 2) for _ in labels]
    colors = [f'hsl({i * 360 // len(labels)},70%,50%)' for i in range(len(labels))]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hoverinfo='label+percent+value',
        textinfo='label+percent',
        marker=dict(colors=colors, line=dict(color='#000000', width=2)),
        pull=pulls
    )])
    fig.update_layout(
        title='Detected Attack Types',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

@app.route('/')
def dashboard():
    real_ips = []
    try:
        for iface, snics in psutil.net_if_addrs().items():
            for snic in snics:
                if snic.family == 2:  # IPv4
                    real_ips.append({
                        'interface': iface,
                        'ip': snic.address,
                        'netmask': snic.netmask
                    })
    except Exception as e:
        print(f"psutil error: {e}")

    connected_ips = get_connected_devices()

    network_logs = generate_and_store_logs()

    malicious_ips, attack_stats = detect_malicious_ips(network_logs)
    attack_chart = create_interactive_attack_chart(attack_stats)

    return render_template(
        'dashboard.html',
        real_ips=real_ips,
        connected_ips=connected_ips,
        malicious_ips=malicious_ips,
        attack_stats=attack_stats,
        attack_chart=attack_chart
    )

@app.route('/logs')
def logs():
    logs = generate_and_store_logs()
    return render_template('logs.html', logs=logs)

@app.route('/download_logs')
def download_logs():
    logs = generate_and_store_logs()
    df = pd.DataFrame(logs)
    csv = df.to_csv(index=False)
    return make_response(csv, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=network_logs.csv'
    })

@app.route('/mitigate', methods=['POST'])
def mitigate():
    ip_address = request.form.get('ip_address')
    action = request.form.get('action', 'block')
    if action == 'block':
        mitigated_ips.add(ip_address)
    return jsonify({
        'status': 'success',
        'message': f'IP {ip_address} has been {action}ed successfully'
    })

@app.route('/update_data')
def update_data():
    logs = generate_and_store_logs()
    malicious_ips, attack_stats = detect_malicious_ips(logs)
    attack_chart = create_interactive_attack_chart(attack_stats)
    return jsonify({
        'malicious_ips': malicious_ips,
        'attack_stats': attack_stats,
        'attack_chart': attack_chart
    })

if __name__ == '__main__':
    app.run(debug=True, threaded=True)