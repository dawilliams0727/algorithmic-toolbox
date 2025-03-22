def edit_distance(first_string: str, second_string: str) -> int:
    """
    Computes the minimum number of edits (insertions, deletions, or substitutions)
    required to convert one string into another.

    Args:
        first_string (str): The source string.
        second_string (str): The target string.

    Returns:
        int: The edit distance between the two strings.
    """
    # you can either remove the previous symbol, insert a space at the previous symbol,
    # or change the previous symbol to get to the current symbol
    n: int = len(first_string)
    m: int = len(second_string)
    table: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]

    # initialize base cases: transforming to/from empty string
    for i in range(n + 1):
        table[i][0] = i
    for j in range(m + 1):
        table[0][j] = j

    # fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion: int = table[i][j - 1] + 1
            deletion: int = table[i - 1][j] + 1
            is_match: int = table[i - 1][j - 1]
            mismatch: int = is_match + 1

            if first_string[i - 1] == second_string[j - 1]:
                table[i][j] = is_match
            else:
                table[i][j] = min(insertion, deletion, mismatch)

    def print_table():
        print("  ", second_string)
        for i, row in enumerate(table):
            prefix = first_string[i - 1] if i > 0 else " "
            print(prefix, row)

    # Uncomment below for debugging table:
    # print_table()

    return table[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
