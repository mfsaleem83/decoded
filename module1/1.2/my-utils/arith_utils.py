def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (i.e., n!).
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_even(n):
    """
    Check if the number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n % 2 == 0:
        return True
    else:
        return False
