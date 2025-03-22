def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_huge_fast(n: int, m: int) -> int:
    """
    Calculates the nth Fibonacci number modulo m using Pisano periods.

    Args:
        n (int): The index of the Fibonacci number.
        m (int): The modulus.

    Returns:
        int: The value of F(n) modulo m.
    """
    period: int
    fib: list[int]
    period, fib = pisano_period(m)
    # Fn % m = F(n % period) % m
    remainder = n % period
    while len(fib) < period:
        fib.append(fib[-1] + fib[-2])
    return fib[remainder] % m
    
def pisano_period(modulus: int) -> tuple[int, list[int]]:
    """
    Computes the length of the Pisano period for a given modulus and returns the Fibonacci sequence up to that point.

    Args:
        modulus (int): The modulus to compute the Pisano period for.

    Returns:
        tuple[int, list[int]]: A tuple containing the length of the Pisano period and the list of Fibonacci numbers up to that point.
    """
    # Pisano period starts with 01 always
    # create memo to store Fn: Fn % m
    # iterate until memo[-2:] == [0,1]
    # period = len(memo) - 2
    if modulus < 2:
        return 1
    mod: list[int] = [0,1]
    fib_memo: list[int] = [0,1]
    fib_memo.append(fib_memo[-1] + fib_memo[-2])
    mod.append(fib_memo[-1] % modulus)
    while mod[-2:] != [0,1]:
        fib_memo.append(fib_memo[-1] + fib_memo[-2])
        mod.append(fib_memo[-1] % modulus)
    return len(mod) - 2, fib_memo

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_fast(n, m))
