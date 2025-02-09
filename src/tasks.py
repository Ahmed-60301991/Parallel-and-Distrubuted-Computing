def worker(process_id):
    print(f"Process {process_id} started")
    # Add your process's code here
    print(f"Process {process_id} finished")


def calculate_sum(n):
    """
    Calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    sum_value = sum(range(1, n + 1))
    return sum_value
