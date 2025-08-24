## 🛡️ Intrusion Detection & Prevention System (IDPS) Network Dashboard
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![Flask](https://img.shields.io/badge/Flask-WebApp-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/) 
[![Bootstrap](https://img.shields.io/badge/Bootstrap-Frontend-purple?logo=bootstrap&logoColor=white)](https://getbootstrap.com/) 
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 
[![CSS3](https://img.shields.io/badge/CSS3-Styles-blue?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) 
[![HTML5](https://img.shields.io/badge/HTML5-Templates-orange?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML) 
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb&logoColor=white)](https://www.mongodb.com/) 
[![Pandas](https://img.shields.io/badge/Data-Pandas-lightgrey?logo=pandas&logoColor=white)](https://pandas.pydata.org/) 
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/python/) 
[![TensorFlow](https://img.shields.io/badge/ML-TensorFlow-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/) 
[![PyTorch](https://img.shields.io/badge/DL-PyTorch-red?logo=pytorch&logoColor=white)](https://pytorch.org/) 
[![Security](https://img.shields.io/badge/IDPS-Security-critical?logo=datadog&logoColor=white)](https://en.wikipedia.org/wiki/Intrusion_detection_system) 
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/yuvarajpanditrathod/IDPS-Network-Dashboard)

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
pip install -r requirements.txt
```

### Step 5: Run the Application

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
## 📑 Reports

A Report [Report.pdf](./Report.pdf)   is included in the repository.
It provides an overview of detected threats, network activity, and mitigation actions. 

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
