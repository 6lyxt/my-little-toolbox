import psutil
import os
import time

CPU_USAGE_THRESHOLD = 0.1
CHECK_INTERVAL = 5

def kill_zombie_processes():
    for proc in psutil.process_iter(['pid', 'status', 'name']):
        try:
            if proc.info['status'] == psutil.STATUS_ZOMBIE:
                print(f"Killing zombie process {proc.info['name']} (PID: {proc.info['pid']})")
                os.kill(proc.info['pid'], 9)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def kill_inactive_processes():
    while True:
        for proc in psutil.process_iter(['pid', 'cpu_percent', 'name']):
            try:
                initial_cpu = proc.cpu_percent(interval=None)
                time.sleep(CHECK_INTERVAL)
                final_cpu = proc.cpu_percent(interval=None)
                if final_cpu < CPU_USAGE_THRESHOLD:
                    print(f"Killing inactive process {proc.info['name']} (PID: {proc.info['pid']}) with CPU usage {final_cpu}%")
                    os.kill(proc.info['pid'], 9)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

if __name__ == "__main__":
    kill_zombie_processes()
    kill_inactive_processes()
