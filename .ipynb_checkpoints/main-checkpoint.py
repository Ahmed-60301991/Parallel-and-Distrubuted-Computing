# Main file to run both threading or multiprocessing code

import sys
import os
from src.threads import *
from src.multiprocessors import *
from src.performance import *
run_threads()
run_multiprocessing()
performance_analysis()
