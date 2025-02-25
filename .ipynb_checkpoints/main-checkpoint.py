import threading
import time
from src.sensor import simulate_sensor, initialize_sensors
from src.processing import process_temperatures
from src.display import initialize_display, update_display

def main():
    num_sensors = 7  # Number of sensors

    # Initialize sensors
    initialize_sensors(num_sensors)

    # Initialize display
    initialize_display(num_sensors)

    # Create and start sensor threads
    sensor_threads = []
    for sensor_id in range(1, num_sensors + 1):
        thread = threading.Thread(target=simulate_sensor, args=(sensor_id,), daemon=True)
        sensor_threads.append(thread)
        thread.start()

    # Create and start the processing thread
    process_thread = threading.Thread(target=process_temperatures, daemon=True)
    process_thread.start()

    # Start the display update thread
    display_thread = threading.Thread(target=update_display, args=(num_sensors,), daemon=True)
    display_thread.start()

    # Keep the main thread alive to allow daemon threads to run
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping simulation...")

if __name__ == "__main__":
    main()
