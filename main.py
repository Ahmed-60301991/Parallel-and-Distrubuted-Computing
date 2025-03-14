from src.sequential import run_sequential
from src.multiprocessing import (
    run_multiprocessing_process, 
    run_multiprocessing_pool_map, 
    run_multiprocessing_pool_apply, 
    run_process_pool_executor
)
from src.semaphores import run_semaphore_test

if __name__ == "__main__":
    print("\n=== Running Square Computations ===")
    
    print("\nSequential Execution:")
    time_seq = run_sequential()
    print(f"Time Taken: {time_seq:.4f} seconds")

    print("\nMultiprocessing (one process per number):")
    time_mp_proc = run_multiprocessing_process()
    print(f"Time Taken: {time_mp_proc:.4f} seconds")

    print("\nMultiprocessing Pool (map):")
    time_mp_pool_map = run_multiprocessing_pool_map()
    print(f"Time Taken: {time_mp_pool_map:.4f} seconds")

    print("\nMultiprocessing Pool (apply):")
    time_mp_pool_apply = run_multiprocessing_pool_apply()
    print(f"Time Taken: {time_mp_pool_apply:.4f} seconds")

    print("\nProcessPoolExecutor:")
    time_executor = run_process_pool_executor()
    print(f"Time Taken: {time_executor:.4f} seconds")

    print("\n=== Running Semaphore-Based Connection Pool ===")
    run_semaphore_test()