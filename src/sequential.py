import time
import random
from src.square import square

def run_sequential():
    """Computes squares sequentially for 1 million numbers."""
    numbers = [random.randint(1, 100) for _ in range(10**6)]  # ✅ Ensure 1M numbers

    start = time.time()
    results = [square(num) for num in numbers]  # ✅ Make sure this actually runs
    end = time.time()

    print(f"Processed {len(results)} numbers.")
    return end - start
