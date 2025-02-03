import random
import string

# Function to join a thousand random letters
# def join_random_letters():
#     letters = [random.choice(string.ascii_letters) for _ in range(1000)]
#     joined_letters = ''.join(letters)
#     print("Joined Letters Task Done")

# # Function to add a thousand random numbers
# def add_random_numbers():
#     numbers = [random.randint(1, 100) for _ in range(1000)]
#     total_sum = sum(numbers)
#     print("Add Numbers Task Done")
def join_random_letters(start, end):
    letters = [random.choice(string.ascii_letters) for _ in range(start, end)]
    joined_letters = ''.join(letters)
    print(f"Joined Letters Task Done (from {start} to {end})")

# Function to add random numbers, modified to accept a range
def add_random_numbers(start, end):
    numbers = [random.randint(1, 100) for _ in range(start, end)]
    total_sum = sum(numbers)
    print(f"Add Numbers Task Done (from {start} to {end})")
