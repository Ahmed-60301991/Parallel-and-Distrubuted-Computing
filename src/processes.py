import multiprocessing
import time
from generic import join_random_letters, add_random_numbers  # Import the common functions

def run_processes(num_letters=10000,num_numbers=10000):
    total_start_time = time.time()
    start1 = 0
    end1=num_letter//2
    start2 = num_letter//2
    end2 = mum_letters

    # Create processes for both functions
    process_letters = multiprocessing.Process(target=join_random_letters)
    process_numbers = multiprocessing.Process(target=add_random_numbers)

    # Start the processes
    process_letters.start()
    process_numbers.start()

    # Wait for all processes to complete
    process_letters.join()
    process_numbers.join()

    total_end_time = time.time()
    print(f"Total time taken: {total_end_time - total_start_time} seconds")

if __name__ == "__main__":
    run_processes()
