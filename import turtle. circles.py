def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example
print(is_prime(7))
print(is_prime(10))
