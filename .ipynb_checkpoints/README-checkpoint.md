10**6 Result:
=== Running Square Computations ===

Sequential Execution:
Processed 1000000 numbers.
Time Taken: 0.0800 seconds

Multiprocessing (one process per number):
Processed 1000000 numbers.
Time Taken: 0.0643 seconds

Multiprocessing Pool (map):
Time Taken: 0.0860 seconds

Multiprocessing Pool (apply):
Time Taken: 171.1057 seconds

ProcessPoolExecutor:
Time Taken: 111.6187 seconds

=== Running Semaphore-Based Connection Pool ===
Process 0 waiting for connection...
Process 0 acquired Connection 0
Process 1 waiting for connection...
Process 1 acquired Connection 1
Process 2 waiting for connection...
Process 2 acquired Connection 2
Process 3 waiting for connection...
Process 4 waiting for connection...
Process 2 releasing Connection 2
Process 3 could not acquire a connection.
Process 4 acquired Connection 2
Process 1 releasing Connection 1
Process 0 releasing Connection 0
Process 4 releasing Connection 2

10**7 Result:
=== Running Square Computations ===

Sequential Execution:
Processed 10000000 numbers.
Time Taken: 0.5680 seconds

Multiprocessing (one process per number):
Processed 10000000 numbers.
Time Taken: 0.6344 seconds

Multiprocessing Pool (map):
Time Taken: 0.7665 seconds

Multiprocessing Pool (apply):
Time Taken: 1705.0256 seconds

ProcessPoolExecutor:
Time Taken: 1049.0290 seconds

=== Running Semaphore-Based Connection Pool ===
Process 0 waiting for connection...
Process 0 could not acquire a connection.
Process 1 waiting for connection...
Process 1 acquired Connection 0
Process 2 waiting for connection...
Process 2 acquired Connection 1
Process 3 waiting for connection...
Process 3 acquired Connection 2
Process 4 waiting for connection...
Process 2 releasing Connection 1
Process 4 could not acquire a connection.
Process 3 releasing Connection 2
Process 1 releasing Connection 0

What are your conclusions for the square computations with 10⁶ and 10⁷ numbers?
Sequential execution was efficient for smaller datasets, while multiprocessing with map() and one process per number performed well for larger data, utilizing CPU cores effectively. In contrast, apply() and ProcessPoolExecutor were significantly slower due to high overhead, making them unsuitable for large-scale tasks.

What are your conclusions when testing both synchronous and asynchronous versions in the pool?
The synchronous map() outperformed the asynchronous apply(), as it efficiently managed tasks in parallel. The asynchronous approach caused substantial delays due to its task-by-task execution, making it inefficient for large datasets.

What happens if more processes try to access the pool than there are available connections?
Excess processes were forced to wait until a connection became available. This prevented resource overuse and ensured stable operation.

How does the semaphore prevent race conditions and ensure safe access to the connections?
The semaphore limited the number of active connections, preventing multiple processes from accessing the same resource. Combined with locks, it maintained orderly access, avoiding race conditions and ensuring reliable connection management.