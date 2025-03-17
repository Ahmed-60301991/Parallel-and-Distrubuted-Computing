import time
import random
from src.square import square
numberSize = 10**6 

def run_sequential():
    """Computes squares sequentially for 1 million numbers."""
    numbers = [random.randint(1, 100) for _ in range(numberSize)]

    start = time.time()
    results = [square(num) for num in numbers] 
    end = time.time()

    print(f"Processed {len(results)} numbers.")
    return end - start
