def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_fast(n: int) -> int:
    """
    Computes the last digit of the sum of Fibonacci numbers from F(0) to F(n), inclusive.

    Args:
        n (int): The ending index of the Fibonacci range.

    Returns:
        int: The last digit of the sum from F(0) to F(n).
    """
    # generate pisano sequence for 10, as last digit of fib number is mod 10 and periodic to 60
    pisano_period: list[int] = [0, 1]
    for i in range(2, 60):
        pisano_period.append((pisano_period[i - 1] + pisano_period[i - 2]) % 10)

    # sum of last digits is:
    # sum(pisano_period[: n % 60]) + sum(pisano_period) * (n // 60)
    total: int = sum(pisano_period) * (n // 60)
    total += sum(pisano_period[: (n % 60) + 1])

    return total % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))
