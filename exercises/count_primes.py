def count_primes(n):
    """
    Counts and displays the number of prime numbers from 0 to n (inclusive).
    
    Parameters:
        n (int): The upper limit of the range to check for primes.

    Returns:
        int: The number of prime numbers in the range 0 to n (inclusive).
    """
    if n < 2:
        print("Number of prime numbers: 0")
        return 0

    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))

    print(f"Number of prime numbers: {prime_count}")
    return prime_count

# Example usage:
result = count_primes(10)
print("Returned count:", result)
