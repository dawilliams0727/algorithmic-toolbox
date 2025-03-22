def compute_operations(n: int) -> list[int]:
    """
    Finds the shortest sequence of operations to reach `n` from 1 using only:
    - add 1
    - multiply by 2
    - multiply by 3

    Args:
        n (int): The target number.

    Returns:
        list[int]: The sequence of numbers from 1 to n using the minimal number of operations.
    """
    # base case: to get to 1, just return [1]
    if n == 1:
        return [1]

    # dp[i] = minimum number of operations to reach i
    dp: list[int] = [0, 0]
    # num[i] = previous number used to reach i in optimal path
    num: list[int] = [-1, 0]

    for i in range(2, n + 1):
        # start by assuming we got here via +1
        dp.append(dp[i - 1] + 1)
        num.append(i - 1)

        # check if getting here via *2 is better
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            num[i] = i // 2

        # check if getting here via *3 is better
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            num[i] = i // 3

    # reconstruct path from n backwards using num[]
    curr: int = num[n]
    path: list[int] = [curr]

    while path[-1] != 1:
        path.append(num[curr])
        curr = path[-1]

    path.reverse()
    path.append(n)

    return path



if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
