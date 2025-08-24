import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    BOOTSTRAP_SERVE_LOCAL = True
    MONGO_URI = "mongodb://localhost:27017/network_dashboard"   