import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.config/.env')

srt_member_number = os.environ.get('srt_member_number')
srt_password = os.environ.get('srt_password')
departure = os.environ.get('departure')
arrival = os.environ.get('arrival')
reserve_date = os.environ.get('reserve_date')
reserve_time = os.environ.get('reserve_time')
max_find = os.environ.get('max_find')
slack_notification_webhook = os.environ.get('slack_notification_webhook')
