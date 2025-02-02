import threading
import time
from generic import join_random_letters, add_random_numbers  # Import the common functions

def run_threads():
    total_start_time = time.time()

    # Create threads for both functions
    thread_letters = threading.Thread(target=join_random_letters)
    # thread_letters = threading.Thread(target=join_random_letters)
    thread_numbers = threading.Thread(target=add_random_numbers)

    # Start the threads
    thread_letters.start()
    thread_numbers.start()

    # Wait for all threads to complete
    thread_letters.join()
    thread_numbers.join()

    total_end_time = time.time()
    print(f"Total time taken: {total_end_time - total_start_time} seconds")

if __name__ == "__main__":
    run_threads()
