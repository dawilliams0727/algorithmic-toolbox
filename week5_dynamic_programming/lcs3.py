def lcs3(first_sequence: list[int], second_sequence: list[int], third_sequence: list[int]) -> int:
    """
    Computes the length of the longest common subsequence (LCS) among three sequences.

    Args:
        first_sequence (list[int]): The first sequence of integers.
        second_sequence (list[int]): The second sequence of integers.
        third_sequence (list[int]): The third sequence of integers.

    Returns:
        int: The length of their longest common subsequence.
    """
    n: int = len(first_sequence)
    m: int = len(second_sequence)
    o: int = len(third_sequence)

    # 3D DP table
    dp: list[list[list[int]]] = [[[0] * (o + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, o + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1]
                    )

    return dp[n][m][o]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
