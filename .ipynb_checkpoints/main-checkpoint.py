import time
import random
from src.threads import *
from src.multiprocessors import *
from src.sequential import *
from src.performance import *
"""
Runs the summation functions sequentially, using threads, and using processes.
Measures execution time for each approach and prints the results.
"""
if __name__ == "__main__":
    n = 10**8
    performance_analysis(n)