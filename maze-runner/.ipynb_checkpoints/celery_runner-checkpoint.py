# celery_runner.py
import argparse
from src.tasks import explorer_task_celery
from src.utils import compare_results  # if compare_results is modularized
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--explorers", type=int, default=4, help="Number of explorers to run")
    parser.add_argument("--visualize", action="store_true", help="Visualize explorer movement")
    args = parser.parse_args()

    maze_type = "static"
    width, height = 30, 30

    # Submit tasks to Celery
    async_results = [
        explorer_task_celery.delay(maze_type, width, height, args.visualize)
        for _ in range(args.explorers)
    ]

    print("Tasks submitted to Celery... waiting for results.")

    # Collect results
    results = []
    for result in async_results:
        results.append(result.get())  # blocks until task finishes

    compare_results(results)

if __name__ == "__main__":
    main()