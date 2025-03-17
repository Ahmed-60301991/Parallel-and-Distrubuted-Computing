import time
import random
from multiprocessing import Process, Queue, Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor
from src.square import square
numberSize = 10**6 

def worker(nums, queue):
    """Worker function to compute squares and store in queue."""
    results = [square(num) for num in nums]
    queue.put(results)

def run_multiprocessing_process():
    """Multiprocessing with a limited number of processes."""
    numbers = [random.randint(1, 100) for _ in range(numberSize)]
    num_workers = min(cpu_count(), 8)  # ✅ Use CPU cores but limit to 8
    chunk_size = len(numbers) // num_workers

    queue = Queue()
    processes = []

    start = time.time()

    for i in range(num_workers):
        chunk = numbers[i * chunk_size: (i + 1) * chunk_size]
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
    """Multiprocessing: Pool with map()"""
    numbers = [random.randint(1, 100) for _ in range(numberSize)]

    start = time.time()
    with Pool() as pool:
        results = pool.map(square, numbers)
    end = time.time()

    return end - start

def run_multiprocessing_pool_apply():
    """Multiprocessing: Pool with apply()"""
    numbers = [random.randint(1, 100) for _ in range(numberSize)]

    start = time.time()
    with Pool() as pool:
        results = [pool.apply(square, args=(num,)) for num in numbers]
    end = time.time()

    return end - start

def run_process_pool_executor():
    """Multiprocessing: ProcessPoolExecutor"""
    numbers = [random.randint(1, 100) for _ in range(numberSize)]

    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))
    end = time.time()

    return end - start