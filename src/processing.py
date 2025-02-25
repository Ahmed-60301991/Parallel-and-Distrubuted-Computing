import time
import threading
from src.sensor import temperature_queues, latest_temperatures, data_lock

# Stores computed moving averages
temperature_averages = {}

def calculate_average_temperature(readings):
    """Calculates the average of the temperature readings."""
    return round(sum(readings) / len(readings), 2) if readings else "--"

def process_temperatures():
    """Processes temperature data and computes moving averages."""
    while True:
        with data_lock:
            for sensor_id, temps in temperature_queues.items():
                temperature_averages[sensor_id] = calculate_average_temperature(list(temps))
        
        time.sleep(1)  # Process data every second
