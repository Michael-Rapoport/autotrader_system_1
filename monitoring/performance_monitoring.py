# monitoring/performance_monitoring.py
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)

def send_slack_notification(message, slack_token, slack_channel):
   client = WebClient(token=slack_token)
   
   try:
       response = client.chat_postMessage(
           channel=slack_channel,
           text=message
       )
   except SlackApiError as e:
       logger.error(f"Error sending Slack notification: {e}")


def monitor_performance(port=8000):
    start_http_server(port)
    
    sharpe_ratio_gauge = Gauge('sharpe_ratio', 'Sharpe Ratio')
    
    while True:
        # Calculate Sharpe ratio
        sharpe_ratio = calculate_sharpe_ratio()
        
        # Update Prometheus gauge
        sharpe_ratio_gauge.set(sharpe_ratio)
        
        time.sleep(60)  # Update every 60 seconds

