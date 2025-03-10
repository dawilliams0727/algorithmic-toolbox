def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_fast(n):
    # the last digit of sum of squares of n fibonacci numbers i s equal to
    # (pisano_period[n // 60] + pisano_perioud[n-1 // 60]) * pisano_period[n // 60] % 10
    # since you're taking mod 60, the majority of the fibonacci can be ignored and the pisano sequence can be used
    pisano_period = [0, 1]
    for i in range(2, 60):
        pisano_period.append((pisano_period[i - 1] + pisano_period[i - 2]) % 10)
    l,w = pisano_period[n % 60], pisano_period[(n-1) % 60]
    return (l+w) * l % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))
