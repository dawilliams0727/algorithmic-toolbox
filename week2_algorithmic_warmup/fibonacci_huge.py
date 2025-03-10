def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_huge_fast(n, m):
    """Calculate the nth Fibonacci number modulo m."""
    # find the period of the modulo m sequence
    period, fib = pisano_period(m)
    # Fn % m = F(n % period) % m
    remainder = n % period
    while len(fib) < period:
        fib.append(fib[-1] + fib[-2])
    return fib[remainder] % m
    
def pisano_period(modulus):
    # Pisano period starts with 01 always
    # create memo to store Fn: Fn % m
    # iterate until memo[-2:] == [0,1]
    # period = len(memo) - 2
    if modulus < 2:
        return 1
    mod = [0,1]
    fib_memo = [0,1]
    fib_memo.append(fib_memo[-1] + fib_memo[-2])
    mod.append(fib_memo[-1] % modulus)
    while mod[-2:] != [0,1]:
        fib_memo.append(fib_memo[-1] + fib_memo[-2])
        mod.append(fib_memo[-1] % modulus)
    return len(mod) - 2, fib_memo

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_fast(n, m))
