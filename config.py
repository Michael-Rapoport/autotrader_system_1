# config.py
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=os.environ.get('LOG_LEVEL', 'INFO'), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# General configuration
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Data configuration
DATA_SOURCE = os.environ.get('DATA_SOURCE', 'iexfinance')
START_DATE = os.environ.get('START_DATE', '2020-01-01')
END_DATE = os.environ.get('END_DATE', '2021-12-31')
TICKERS = os.environ.get('TICKERS', 'AAPL').split(',')

# Trading configuration
INITIAL_CAPITAL = int(os.environ.get('INITIAL_CAPITAL', '100000'))
RISK_TOLERANCE = float(os.environ.get('RISK_TOLERANCE', '0.02'))

# Broker configuration
BROKER = os.environ.get('BROKER', 'interactive_brokers')
IB_HOST = os.environ.get('IB_HOST', '127.0.0.1')
IB_PORT = int(os.environ.get('IB_PORT', '7497'))
IB_CLIENT_ID = int(os.environ.get('IB_CLIENT_ID', '1'))

# Monitoring configuration
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL', '#trading-notifications')

# MLOps configuration
MLFLOW_TRACKING_URI = os.environ.get('MLFLOW_TRACKING_URI')
MODEL_NAME = os.environ.get('MODEL_NAME', 'ensemble_model')
MODEL_VERSION = os.environ.get('MODEL_VERSION', '1.0.0')

