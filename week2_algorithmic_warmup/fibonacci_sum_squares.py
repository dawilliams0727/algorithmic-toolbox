def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_fast(n: int) -> int:
    """
    Computes the last digit of the sum of squares of Fibonacci numbers from F(0)^2 to F(n)^2.

    Args:
        n (int): The ending index of the Fibonacci sequence.

    Returns:
        int: The last digit of the sum of squares of Fibonacci numbers up to F(n).
    """
    # the last digit of sum of squares of n fibonacci numbers is equal to
    # (F(n) * F(n+1)) % 10
    # since you're taking mod 10, you can use the Pisano period of 60
    pisano_period: list[int] = [0, 1]
    for i in range(2, 60):
        pisano_period.append((pisano_period[i - 1] + pisano_period[i - 2]) % 10)

    l: int = pisano_period[n % 60]
    w: int = pisano_period[(n - 1) % 60]

    return (l + w) * l % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))
