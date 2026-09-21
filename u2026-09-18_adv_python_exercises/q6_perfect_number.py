def is_perfect(number: int) -> bool:
    """Check if a number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    if number <= 1:
        return False

    divisors = [i for i in range(1, number) if number % i == 0]

    return sum(divisors) == number

if __name__ == "__main__":
    test_numbers = [1,2,3,6, 28, 496, 1000, 8128, 12, 237, 854, 901, 8000, 97]

    for num in test_numbers:
        print(f"{num}: \t {'is' if is_perfect(num) else 'is not'} a perfect number.")