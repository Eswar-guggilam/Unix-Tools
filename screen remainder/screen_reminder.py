import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

# Configure notification details
app_name = "Notification App"
summary = "Friendly Reminder"
message = "Time to take a break!"
icon_path = "/home/shiva/Pictures/icon.png"  # Replace with the path to your icon (optional)

def show_notification():
  """Displays a notification with the specified message."""
  try:
    Notify.init(app_name)
    notification = Notify.Notification.new(summary, message, icon_path)
    notification.show()
  except Exception as e:
    print(f"Error showing notification: {e}")

# Schedule notification using cron
import schedule
import time

def run_every_20_minutes():
  """Calls the show_notification function every 20 minutes."""
  show_notification()

schedule.every(20).minutes.do(run_every_20_minutes)

while True:
  schedule.run_pending()
  time.sleep(1)

# Make the script executable (optional)
# chmod +x notification_script.py
