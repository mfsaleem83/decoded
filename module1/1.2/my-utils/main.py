from arith_utils import factorial, is_prime, is_even

# List of numbers to analyze
numbers = [3, 5, 10]

# Loop through each number and print:
# the factorial of the number
# whether it is a prime number
for n in numbers:
    print(f"{n}! = {factorial(n)}, Prime? {is_prime(n)}")
    print(f"Is Even {is_even(n)} ")
