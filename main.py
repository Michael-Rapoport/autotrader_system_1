# main.py
import logging
from config import (
   DEBUG, DATA_SOURCE, START_DATE, END_DATE, TICKERS, INITIAL_CAPITAL, RISK_TOLERANCE,
   BROKER, IB_HOST, IB_PORT, IB_CLIENT_ID,
   SLACK_TOKEN, SLACK_CHANNEL,
   MLFLOW_TRACKING_URI, MODEL_NAME, MODEL_VERSION
)
from data.data_preprocessing import fetch_raw_data, preprocess_data
from models.ensemble.ensemble_model import create_ensemble_model
from strategies.mean_reversion.mean_reversion_strategy import mean_reversion_strategy
from backtesting.backtesting_engine import backtest_strategy, analyze_performance
from risk_management.risk_metrics import calculate_value_at_risk, calculate_expected_shortfall
from execution.interactive_brokers.ib_execution import execute_order
from monitoring.performance_monitoring import send_slack_notification
from mlops.model_deployment import deploy_model

logger = logging.getLogger(__name__)

def main():
   try:
       # Data preprocessing
       raw_data = {}
       processed_data = {}
       for ticker in TICKERS:
           raw_data[ticker] = fetch_raw_data(ticker)
           processed_data[ticker] = preprocess_data(raw_data[ticker])
       
       # Model training
       lstm_input_shape = (60, len(processed_data[TICKERS[0]].columns) - 1)
       xgboost_input_shape = lstm_input_shape
       ensemble_model = create_ensemble_model(lstm_input_shape, xgboost_input_shape)
       ensemble_model.fit(processed_data, epochs=50, batch_size=32)
       
       # Strategy backtesting
       strategy = mean_reversion_strategy
       portfolio = backtest_strategy(strategy, processed_data, INITIAL_CAPITAL)
       performance_stats = analyze_performance(portfolio['returns'])
       
       # Risk management
       var = calculate_value_at_risk(portfolio['returns'])
       es = calculate_expected_shortfall(portfolio['returns'], confidence_level=1 - RISK_TOLERANCE)
       
       # Execution
       if BROKER == 'interactive_brokers':
           ib = IB()
           ib.connect(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)
           for ticker in TICKERS:
               trade = execute_order(ib, ticker, 100, 'BUY')
               send_slack_notification(f"New trade executed: {trade}", SLACK_TOKEN, SLACK_CHANNEL)
           ib.disconnect()
       
       # Model deployment
       deploy_model(ensemble_model, MODEL_NAME, MODEL_VERSION, MLFLOW_TRACKING_URI)
       
   except Exception as e:
       logger.error(f"Error in main: {e}")
       if DEBUG:
           raise e

if __name__ == '__main__':
   main()
