import sys
import time
import threading
from src.sensor import latest_temperatures, data_lock
from src.processing import temperature_averages

# def initialize_display(num_sensors):
#     """Initializes the console display layout."""
#     print("Current temperatures:")
#     print("Latest Temperatures: ", end="")
#     for i in range(1, num_sensors + 1):
#         print(f"Sensor {i}: --°C", end=" ")
#     print()
#     for i in range(1, num_sensors + 1):
#         print(f"Sensor {i} Average: --°C")
#     print("\nDisplaying initial layout...\n")

# def update_display(num_sensors):
#     """Updates the console display with the latest sensor readings."""
#     while True:
#         with data_lock:
#             sys.stdout.write("\rLatest Temperatures: ")
#             for i in range(1, num_sensors + 1):
#                 temp = latest_temperatures.get(i, "--")
#                 sys.stdout.write(f"Sensor {i}: {temp}°C  ")

#             sys.stdout.write("\n")
#             for i in range(1, num_sensors + 1):
#                 avg_temp = temperature_averages.get(i, "--")
#                 print(f"Sensor {i} Average: {avg_temp}°C")

#             sys.stdout.flush()
        
#         time.sleep(5)  # Update display every 5 seconds

def initialize_display(num_sensors):
    """Initializes the console display layout."""
    print("Current temperatures:")
    print("Latest Temperatures: ", end="")
    for i in range(1, num_sensors + 1):
        print(f"Sensor {i}: --°C", end=" ")
    print()
    for i in range(1, num_sensors + 1):
        print(f"Sensor {i} Average: --°C")
    print("\nDisplaying initial layout...\n")

def update_display(num_sensors):
    """Updates the console display with latest temperatures every second and averages every 5 seconds."""
    last_avg_update = time.time()

    while True:
        with data_lock:
            sys.stdout.write("\rLatest Temperatures: ")
            for i in range(1, num_sensors + 1):
                temp = latest_temperatures.get(i, "--")
                sys.stdout.write(f"Sensor {i}: {temp}°C  ")

            sys.stdout.flush()
        
        # Check if 5 seconds have passed to update averages
        if time.time() - last_avg_update >= 5:
            print("\n", end="")  # Move to new line before printing averages
            with data_lock:
                for i in range(1, num_sensors + 1):
                    avg_temp = temperature_averages.get(i, "--")
                    print(f"Sensor {i} Average: {avg_temp}°C", end="  ")
                print("\n")  # New line after averages
            
            last_avg_update = time.time()

        time.sleep(1)  # Update latest temperatures every second