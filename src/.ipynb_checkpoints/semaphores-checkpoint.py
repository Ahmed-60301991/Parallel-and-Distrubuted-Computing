import time
import random
from multiprocessing import Semaphore, Process, Lock, Queue


class ConnectionPool:
    """
    Simulates a limited pool of database connections using semaphores.

    Attributes:
        semaphore (Semaphore): Controls access to the pool.
        queue (Queue): Ensures FIFO ordering of connections.
        lock (Lock): Prevents race conditions when modifying the queue.
    """
    def __init__(self, size):
        self.semaphore = Semaphore(size)
        self.lock = Lock() 
        self.queue = Queue()

        # Populate the queue with connections
        for i in range(size):
            self.queue.put(f"Connection {i}")

    def get_connection(self):
        """
        Acquire a unique connection safely.

        Returns:
            str: Connection ID if available, else None.
        """
        self.semaphore.acquire()
        with self.lock: 
            if not self.queue.empty():
                return self.queue.get()
            else:
                self.semaphore.release() 
                return None

    def release_connection(self, conn):
        """
        Release a connection back to the pool.

        Parameters:
            conn (str): Connection ID to be released.
        """
        if conn:
            with self.lock:
                self.queue.put(conn)
            self.semaphore.release()

def access_database(pool, process_id):
    """
    Simulates a process performing a database operation.

    Parameters:
        pool (ConnectionPool): The connection pool instance.
        process_id (int): The ID of the process.
    """
    print(f"Process {process_id} waiting for connection...")
    conn = pool.get_connection()
    if conn:
        print(f"Process {process_id} acquired {conn}")
        time.sleep(random.uniform(1, 3))  # Simulate database work
        print(f"Process {process_id} releasing {conn}")
        pool.release_connection(conn)
    else:
        print(f"Process {process_id} could not acquire a connection.")

def run_semaphore_test():
    """
    Runs the semaphore-based connection pool test with multiple processes.
    """
    pool_size = 3
    num_processes = 5
    pool = ConnectionPool(pool_size)
    
    processes = [Process(target=access_database, args=(pool, i)) for i in range(num_processes)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
