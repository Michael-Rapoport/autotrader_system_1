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

