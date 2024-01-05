import requests
from config import slack_notification_webhook

def send_notification(username, msg):
    try:
        data = {"username": username, "text": msg}
        response = requests.post(slack_notification_webhook, json=data)
        print(f'{response}')
        return
    except Exception as e:
        print("Error occur while sending message to slack")
        print(f'{e}')
        return
