def sum_of_two_digits(first_digit: int, second_digit: int) -> int:
    """
    Returns the sum of two digits.

    Args:
        first_digit (int): The first digit.
        second_digit (int): The second digit.

    Returns:
        int: The sum of the two digits.
    """
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
    
