import random


def max_pairwise_product(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

def generate(N,M):
    n = N
    array = []
    for i in range (n):
        array.append(random.randint(0,M))
    return array

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
    
