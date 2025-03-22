def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number_fast(n: int) -> int:
    """
    Computes the nth Fibonacci number using an iterative approach with memoization.

    Args:
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    memo: list[int] = [0, 1]
    if n <= 1:
        return n

    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])

    return memo[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_fast(input_n))
