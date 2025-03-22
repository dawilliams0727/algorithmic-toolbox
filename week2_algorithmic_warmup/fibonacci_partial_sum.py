# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_partial_sum_fast(from_, to):
    # generate pisano sequence for 10, as last digit of fib number is mod 10 and periodic to 60 (pisano period)
    pisano_period = [0, 1]
    for i in range(2, 60):
        pisano_period.append((pisano_period[i - 1] + pisano_period[i - 2]) % 10)
    # sum is last digits is sum(pisano_period[: n % 60]) + sum(pisano_period) * (n // 60)
    total = sum(pisano_period) * (to // 60)
    total += sum(pisano_period[: (to % 60) + 1])
    total -= sum(pisano_period[: (from_ % 60)])
    return total % 10

if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
