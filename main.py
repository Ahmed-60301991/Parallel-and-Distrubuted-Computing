import random
import time
import os
import threading
from collections import deque
import sys

# Global dictionaries to store the latest temperatures from each sensor and the calculated averages
latest_temperatures = {}
temperature_averages = {}

# Queue size for the number of readings to store for averaging
QUEUE_SIZE = 5

# Function to simulate temperature reading from a sensor
def simulate_sensor(sensor_id):
    while True:
        # Generate a random temperature between 15°C and 40°C
        temperature = random.randint(15, 40)
        # Update the global dictionary with the sensor's temperature
        latest_temperatures[sensor_id] = temperature
        time.sleep(1)  # Simulate sensor reading every second

# Function to calculate the average temperature
def calculate_average_temperature(readings):
    return round(sum(readings) / len(readings), 2)

# Function to initialize the display layout
def initialize_display(num_sensors):
    print("Current temperatures:")
    print("Latest Temperatures: ", end="")
    for i in range(1, num_sensors + 1):
        print(f"Sensor {i}: --°C", end=" ")
    print()
    for i in range(1, num_sensors + 1):
        print(f"Sensor {i} Average: --°C")
    print("\nDisplaying initial layout...\n")

# Function to update the display with the latest readings and averages
def update_display(num_sensors):
    sys.stdout.write("\rLatest Temperatures: ")
    for i in range(1, num_sensors + 1):
        temp = latest_temperatures.get(i, "--")
        print(f"Sensor {i}: {temp}°C", end=" ")

    sys.stdout.write("\n")
    for i in range(1, num_sensors + 1):
        avg_temp = temperature_averages.get(i, "--")
        print(f"Sensor {i} Average: {avg_temp}°C")

# Function to process temperatures and update the temperature averages
def process_temperatures():
    global temperature_averages
    
    # Create a deque for each sensor to store recent temperature readings
    for sensor_id in latest_temperatures:
        if sensor_id not in temperature_averages:
            temperature_averages[sensor_id] = deque(maxlen=QUEUE_SIZE)
    
    while True:
        # Add the latest temperature to the corresponding sensor's deque
        for sensor_id, temp in latest_temperatures.items():
            temperature_averages[sensor_id].append(temp)
        
        # Calculate the average temperature for each sensor and update the global dictionary
        for sensor_id, temps in temperature_averages.items():
            if temps:  # Avoid division by zero
                avg_temp = calculate_average_temperature(list(temps))
                temperature_averages[sensor_id] = avg_temp  # Store the average value in the dictionary

        time.sleep(1)  # Process temperatures every second

# Main function to simulate and update sensors
def main():
    num_sensors = 7  # Set the number of sensors to 7
    
    # Initialize the latest_temperatures dictionary with sensor IDs and initial temperatures
    for i in range(1, num_sensors + 1):
        latest_temperatures[i] = random.randint(15, 40)
    
    # Initialize display with placeholders for temperatures and averages
    initialize_display(num_sensors)

    # Create and start threads for simulating sensors
    sensor_threads = []
    for sensor_id in range(1, num_sensors + 1):
        thread = threading.Thread(target=simulate_sensor, args=(sensor_id,), daemon=True)
        sensor_threads.append(thread)
        thread.start()

    # Create and start the process_temperatures thread
    process_thread = threading.Thread(target=process_temperatures, daemon=True)
    process_thread.start()
    
    # Start the simulation and update the display in real-time
    while True:
        # Update the display with the latest sensor readings and averages
        update_display(num_sensors)
        
        # Update every 1 second
        time.sleep(1)

if __name__ == "__main__":
    main()
