def lcs2(first_sequence: list[int], second_sequence: list[int]) -> int:
    """
    Computes the length of the longest common subsequence (LCS) between two sequences.

    Args:
        first_sequence (list[int]): The first sequence of integers.
        second_sequence (list[int]): The second sequence of integers.

    Returns:
        int: The length of their longest common subsequence.
    """
    n: int = len(first_sequence)
    m: int = len(second_sequence)
    dp: list[list[int]] = [[0 for _ in range(m)] for _ in range(n)]

    # initialize first cell
    if first_sequence[0] == second_sequence[0]:
        dp[0][0] = 1

    # initialize first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0]
        if first_sequence[i] == second_sequence[0]:
            dp[i][0] = 1

    # initialize first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1]
        if first_sequence[0] == second_sequence[j]:
            dp[0][j] = 1

    # fill DP table
    for i in range(1, n):
        for j in range(1, m):
            if first_sequence[i] == second_sequence[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Uncomment to visualize the table:
    # print(" ", second_sequence)
    # for i, row in enumerate(dp): print(f"{first_sequence[i]}{row}")

    return dp[n - 1][m - 1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
