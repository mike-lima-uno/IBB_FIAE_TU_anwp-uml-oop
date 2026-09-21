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
    test_numbers = [1,2,3,6, 12, 97, 28, 237, 496, 854, 901, 1000, 8000, 8128]

    for num in test_numbers:
        print(f"{num}: \t {'is' if is_perfect(num) else "ISN'T"} a perfect number.")