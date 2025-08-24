# IDSP Network Dashboard

## 🛡️ Intrusion Detection System & Prevention (IDSP) Network Dashboard

A comprehensive network security monitoring dashboard that combines machine learning-based intrusion detection with real-time network monitoring capabilities. This system provides automated threat detection, anomaly analysis, and network traffic visualization through an intuitive web interface.

## 🚀 Features

- **Real-time Network Monitoring**: Live system performance and network traffic analysis
- **Machine Learning-based Threat Detection**: Multiple ML models for anomaly and attack detection
- **Automated Mitigation**: Intelligent response to detected threats
- **Interactive Dashboard**: Web-based interface with real-time data visualization
- **Multi-model Ensemble**: Combines multiple algorithms for improved accuracy
- **Network Device Discovery**: Automatic detection of connected devices
- **Comprehensive Logging**: Detailed logs with MongoDB storage

## 🛠️ Technologies & Tools Used

### Backend Technologies
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for dashboard interface
- **MongoDB**: Database for storing network logs and events
- **PyMongo**: MongoDB driver for Python

### Machine Learning & AI
- **TensorFlow/Keras**: Deep learning models (CNN-LSTM, Autoencoder)
- **PyTorch**: Neural network implementations
- **Scikit-learn**: Traditional ML algorithms (Isolation Forest, Ensemble methods)
- **XGBoost**: Gradient boosting for attack classification
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### Visualization & Frontend
- **Plotly**: Interactive data visualization
- **HTML/CSS/JavaScript**: Frontend technologies
- **Bootstrap**: Responsive UI framework

### System Monitoring
- **psutil**: System and process utilities
- **subprocess**: System command execution
- **socket**: Network programming
- **threading**: Concurrent processing

## 📋 System Requirements

### Minimum System Specifications
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Processor**: Intel i5 or AMD Ryzen 5 (4 cores minimum)
- **RAM**: 8 GB minimum (16 GB recommended)
- **Storage**: 5 GB free disk space
- **Network**: Ethernet or Wi-Fi connection

### Software Dependencies
- **Python**: 3.8 or higher
- **MongoDB**: 4.4 or higher
- **Git**: Latest version for cloning repository

### Hardware Recommendations for Optimal Performance
- **Processor**: Intel i7/AMD Ryzen 7 or higher
- **RAM**: 16 GB or more
- **Storage**: SSD with 10+ GB free space
- **GPU**: CUDA-compatible GPU (optional, for faster ML processing)

## 📁 Project Structure

```
IDSP-Network-Dashboard/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies (to be created)
├── __pycache__/                    # Python cache files
│   └── config.cpython-312.pyc
├── models/                         # Pre-trained ML models
│   ├── anomaly_scaler.pkl          # Anomaly detection scaler
│   ├── attack_feature_scaler.pkl   # Attack classification scaler
│   ├── attack_label_encoder.pkl    # Attack type label encoder
│   ├── autoencoder_model.h5        # Autoencoder for anomaly detection
│   ├── cnn_lstm_model.keras        # CNN-LSTM hybrid model
│   ├── ensemble_voting_model.pkl   # Ensemble voting classifier
│   ├── isolation_forest_model.pkl  # Isolation Forest model
│   ├── label_encoder.pkl           # General label encoder
│   └── xgboost_attack_classifier_weighted.pkl # XGBoost classifier
├── static/                         # Static web assets
│   ├── css/
│   │   └── styles.css              # Custom CSS styles
│   ├── img/                        # Image assets
│   └── js/
│       └── scripts.js              # JavaScript functionality
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   ├── dashboard.html              # Main dashboard
│   └── logs.html                   # Logs viewer
└── testing/                        # Testing and automation scripts
    ├── automate_mitigation_loop.py # Automated mitigation testing
    └── automate_mitigation.py      # Mitigation automation
```

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yuvarajpanditrathod/IDSP-Network-Dashboard.git
cd IDSP-Network-Dashboard
```

### Step 2: Install MongoDB

#### Windows:
1. Download MongoDB Community Server from [MongoDB Download Center](https://www.mongodb.com/try/download/community)
2. Run the installer and follow the setup wizard
3. Start MongoDB service

#### macOS:
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

#### Linux (Ubuntu/Debian):
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
```

### Step 3: Create Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Python Dependencies

```bash
pip install flask pymongo flask-pymongo python-dotenv
pip install pandas numpy matplotlib plotly
pip install tensorflow torch torchvision
pip install scikit-learn xgboost joblib
pip install psutil
```

### Step 5: Environment Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here-change-this-in-production
MONGO_URI=mongodb://localhost:27017/network_dashboard
```

### Step 6: Run the Application

```bash
python app.py
```

The dashboard will be available at: `http://localhost:5000`

## 🖥️ Usage

1. **Access Dashboard**: Open your web browser and navigate to `http://localhost:5000`
2. **Monitor Network**: View real-time network statistics and connected devices
3. **Threat Detection**: Monitor alerts and anomalies detected by ML models
4. **View Logs**: Access detailed network logs in the logs section
5. **Automated Response**: The system automatically responds to detected threats

## 🔧 Configuration

### MongoDB Configuration
- Default connection: `mongodb://localhost:27017/network_dashboard`
- Modify `MONGO_URI` in `config.py` for custom MongoDB setup

### Model Configuration
- Pre-trained models are located in the `models/` directory
- Models are automatically loaded on application startup
- Custom models can be added by updating the `load_models()` function

## 🧪 Testing

Run the automated testing scripts:

```bash
# Run mitigation testing
python testing/automate_mitigation.py

# Run continuous mitigation loop
python testing/automate_mitigation_loop.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **MongoDB Connection Error**: Ensure MongoDB service is running
2. **Model Loading Errors**: Verify all model files are present in `models/` directory
3. **Port Already in Use**: Change the port in `app.py` if 5000 is occupied
4. **Permission Errors**: Run with appropriate permissions for network monitoring

### Performance Optimization

- Use SSD storage for better I/O performance
- Allocate sufficient RAM for ML model processing
- Consider GPU acceleration for TensorFlow operations

## 📧 Support & Contact

For questions, issues, or collaboration opportunities, please reach out to us:

**Email**: [yuvarajpanditrathod@gmail.com](mailto:yuvarajpanditrathod@gmail.com)

Please include the following information in your query:
- Detailed description of the issue
- System specifications
- Error messages (if any)
- Steps to reproduce the problem

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- TensorFlow and PyTorch communities for excellent ML frameworks
- Flask team for the lightweight web framework
- MongoDB for robust document storage
- Plotly for interactive visualizations

---

**⭐ If you find this project helpful, please consider giving it a star on GitHub!**
