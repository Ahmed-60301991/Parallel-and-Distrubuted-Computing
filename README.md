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