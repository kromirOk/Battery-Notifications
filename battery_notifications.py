import psutil
from plyer import notification
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def script_running():
    notification.notify(
        title="Script is running",
        message="You have successfully started the script.",
        timeout = 5
    )

def is_battery_over_80():
    battery = psutil.sensors_battery()
    if battery.power_plugged and battery.percent >= 80:
        notification.notify(title="Unplug the device", message="Your device has reached the charge of 80%, please unplug", timeout=5)
    scheduler.enter(60, 1, is_battery_over_80)

scheduler.enter(0.1, 1, is_battery_over_80)
scheduler.enter(0.1, 2, script_running)

scheduler.run()
