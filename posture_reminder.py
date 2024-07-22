import os
import time
import schedule

def send_notification():
    title = "Posture Reminder"
    message = "Sit straight and take care of your posture!"
    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")

schedule.every().hour.do(send_notification)

while True:
    schedule.run_pending()
    time.sleep(1)
