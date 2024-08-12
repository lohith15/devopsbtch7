
import psutil
import time

def monitor_cpu_usage(threshold=80):
    try:
        print("Monitoring CPU usage...")
        while True:
            # Get the CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            
            # Sleep for a short period before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu_usage(threshold=80)