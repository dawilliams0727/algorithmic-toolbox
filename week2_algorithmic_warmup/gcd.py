def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a: int, b: int) -> int:
    """
    Computes the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    return gcd_fast(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_fast(a, b))
