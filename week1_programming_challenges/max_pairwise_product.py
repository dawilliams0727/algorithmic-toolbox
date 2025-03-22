import random


def max_pairwise_product(numbers: list[int]) -> int:
    """
    Computes the maximum product of any two distinct numbers in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The maximum pairwise product.
    """
    sorted_numbers: list[int] = sorted(numbers)
    return sorted_numbers[-1] * sorted_numbers[-2]

def generate(N,M):
    n: int = N
    array: list[int] = []
    for i in range (n):
        array.append(random.randint(0,M))
    return array

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
