def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fibonacci_last_digit_fast(n):
    # Pisano period for modulo 10 is 60
    # last digit of the nth Fibonacci number is the same as the last digit of the n mod 60th Fibonacci number
    remainder = n % 60
    fib = [0,1]
    for i in range(2, remainder + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[remainder] % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit_fast(n))
