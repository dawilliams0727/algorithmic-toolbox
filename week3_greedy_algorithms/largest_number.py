from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def largest_number(numbers):
    result = ""
    def custom_sort(x):
        if len(x) == 1:
            return x+x
        if x == "100":
            return "00"
        return x
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = custom_sort, reverse = True)
    
    for number in numbers:
        result += number
    return result

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
