# Perfect Number Checker
# A perfect number is equal to the sum of its proper divisors (excluding itself)

def is_perfect(num):
    """Return True if num is a perfect number."""
    if num < 2:
        return False
    divisors_sum = 1  # 1 is always a divisor
    # Only go up to sqrt(num) for efficiency
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:  # avoid adding the square root twice
                divisors_sum += num // i
    return divisors_sum == num

# Example usage
print("Perfect numbers between 1 and 10000:")
for n in range(1, 100000001):
    if is_perfect(n):
        print(n)
