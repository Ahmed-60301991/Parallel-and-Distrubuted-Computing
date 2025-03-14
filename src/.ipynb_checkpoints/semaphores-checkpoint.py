import time
import random
from multiprocessing import Semaphore, Process

class ConnectionPool:
    """Manages a limited number of connections using a semaphore."""
    def __init__(self, size):
        self.semaphore = Semaphore(size)
        self.connections = [f"Connection {i}" for i in range(size)]

    def get_connection(self):
        """Acquire a connection safely."""
        self.semaphore.acquire()
        if self.connections:
            return self.connections.pop()
        else:
            self.semaphore.release()  # Release if no connection available
            return None

    def release_connection(self, conn):
        self.connections.append(conn)
        self.semaphore.release()

def access_database(pool, process_id):
    """Simulates a process performing a database operation."""
    print(f"Process {process_id} waiting for connection...")
    conn = pool.get_connection()
    print(f"Process {process_id} acquired {conn}")

    time.sleep(random.uniform(1, 3))  # Simulate work

    print(f"Process {process_id} releasing {conn}")
    pool.release_connection(conn)

def run_semaphore_test():
    """Runs the semaphore-based connection pool test."""
    pool_size = 3
    num_processes = 5
    pool = ConnectionPool(pool_size)
    
    processes = [Process(target=access_database, args=(pool, i)) for i in range(num_processes)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
