def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def lcm_fast(a: int, b: int) -> int:
    """
    Computes the least common multiple (LCM) of two integers using their GCD.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The least common multiple of a and b.
    """
    gcd: int = gcd_fast(a, b)
    return a * b // gcd

def gcd_fast(a,b):
    if b == 0:
        return a
    return gcd_fast(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

