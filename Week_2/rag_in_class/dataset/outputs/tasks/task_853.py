import math

def sum_of_odd_Factors(n):
    result = 1
    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        current_sum = 1
        current_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            current_term *= i
            current_sum += current_term
        result *= current_sum

    # Handle remaining prime factor (if n is a prime number >= 3)
    if n > 2:
        result *= (1 + n)

    return result
