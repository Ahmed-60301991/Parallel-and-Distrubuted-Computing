import multiprocessing

# Number of processes to create
num_processes = 4

# Create and start processes in a loop
processes = []
for i in range(num_processes):
    process = multiprocessing.Process(target=worker, args=(i,))
    processes.append(process)
    process.start()

# Wait for all processes to finish
for process in processes:
    process.join()

print("All processes have finished")

def process_sum(n, num_processes=4):
    def partial_sum(start, end, queue):
        queue.put(sum(range(start, end)))
    
    processes = []
    chunk_size = n // num_processes
    queue = multiprocessing.Queue()
    
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1 if i != num_processes - 1 else n + 1
        process = multiprocessing.Process(target=partial_sum, args=(start, end, queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    total_sum = sum(queue.get() for _ in range(num_processes))
    return total_sum
