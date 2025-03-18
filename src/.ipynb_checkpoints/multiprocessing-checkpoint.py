import time
import random
from multiprocessing import Process, Queue, Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor
from src.square import square

# Define global variable for list size
NUMBER_SIZE = 10**6  

def worker(nums, queue):
    """
    Worker function to compute squares and store results in a queue.

    Parameters:
        nums (list): List of numbers to square.
        queue (Queue): Queue to store results.
    """
    results = [square(num) for num in nums]
    queue.put(results)

def run_multiprocessing_process():
    """
    Multiprocessing with a limited number of processes.

    Returns:
        float: Execution time in seconds.
    """
    numbers = [random.randint(1, 100) for _ in range(NUMBER_SIZE)]
    num_workers = min(cpu_count(), 8)  # Use CPU cores but limit to 8
    chunk_size = len(numbers) // num_workers

    queue = Queue()
    processes = []

    start = time.time()

    for i in range(num_workers):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i != num_workers - 1 else len(numbers)

        chunk = numbers[start_idx:end_idx]
        p = Process(target=worker, args=(chunk, queue))
        processes.append(p)
        p.start()


    results = []
    for _ in processes:
        results.extend(queue.get())

    for p in processes:
        p.join()

    end = time.time()

    print(f"Processed {len(results)} numbers.")
    return end - start

def run_multiprocessing_pool_map():
    """Multiprocessing using Pool.map()."""
    numbers = [random.randint(1, 100) for _ in range(NUMBER_SIZE)]

    start = time.time()
    with Pool() as pool:
        results = pool.map(square, numbers)
    end = time.time()

    return end - start

def run_multiprocessing_pool_apply():
    """Multiprocessing using Pool.apply_async()."""
    numbers = [random.randint(1, 100) for _ in range(NUMBER_SIZE)]

    start = time.time()
    with Pool() as pool:
        results = [pool.apply(square, args=(num,)) for num in numbers]
    end = time.time()

    return end - start

def run_process_pool_executor():
    """Multiprocessing using ProcessPoolExecutor()."""
    numbers = [random.randint(1, 100) for _ in range(NUMBER_SIZE)]

    start = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(square, numbers))
    end = time.time()

    return end - start
