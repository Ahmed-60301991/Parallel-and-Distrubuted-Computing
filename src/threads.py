import threading

# Number of threads to create
num_threads = 4

# Create and start threads in a loop
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished")

def threaded_sum(n, num_threads=4):
    def partial_sum(start, end, result_list, index):
        result_list[index] = sum(range(start, end))
    
    threads = []
    chunk_size = n // num_threads
    results = [0] * num_threads
    
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1 if i != num_threads - 1 else n + 1
        thread = threading.Thread(target=partial_sum, args=(start, end, results, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return sum(results)
