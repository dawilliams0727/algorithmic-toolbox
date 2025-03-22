def change(money: int) -> int:
    """
    Computes the minimum number of coins needed to make change for a given amount
    using denominations of 1, 3, and 4.

    Args:
        money (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins required.
    """
    # start at base case where min change is easily known
    change: list[int] = [0, 1, 2, 1, 1, 2]

    # for each index (corresponds to amount), choose the minimum coins from [i-1, i-3, i-4]
    for i in range(6, money + 1):
        one: int = change[i - 1] if i - 1 >= 0 else float('inf')
        three: int = change[i - 3] if i - 3 >= 0 else float('inf')
        four: int = change[i - 4] if i - 4 >= 0 else float('inf')
        change.append(min(one, three, four) + 1)

    # return the value at change[money]
    return change[money]



if __name__ == '__main__':
    m = int(input())
    print(change(m))
