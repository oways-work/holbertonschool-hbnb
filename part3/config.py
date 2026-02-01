import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    # Calculate the absolute path to the root directory
    # (Go up one level from config.py to reach 'part3', then up again if needed, or just standard)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # This creates 'development.db' inside the 'part3' folder consistently
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'development.db')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
