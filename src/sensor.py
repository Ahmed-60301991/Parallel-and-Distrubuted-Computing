import random
import time
import threading
from collections import deque

# Shared Data Structures
latest_temperatures = {}
temperature_queues = {}  # Stores deques for each sensor
QUEUE_SIZE = 5

# Lock for synchronizing data access
data_lock = threading.RLock()

def simulate_sensor(sensor_id):
    """Simulates temperature readings from a sensor."""
    while True:
        temperature = random.randint(15, 40)

        with data_lock:
            latest_temperatures[sensor_id] = temperature
            temperature_queues[sensor_id].append(temperature)

        time.sleep(1)  # Simulate reading every second

def initialize_sensors(num_sensors):
    """Initializes sensor storage structures."""
    for i in range(1, num_sensors + 1):
        latest_temperatures[i] = 0  # Default temperature
        temperature_queues[i] = deque(maxlen=QUEUE_SIZE)
