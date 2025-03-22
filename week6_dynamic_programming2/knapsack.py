from sys import stdin


def maximum_gold(capacity: int, weights: list[int]) -> int:
    """
    Solves the 0/1 knapsack problem for gold bars.

    Given a set of gold bars of various weights and a backpack that can hold at most
    `capacity` pounds, this function returns the maximum weight of gold that fits in the backpack.

    Args:
        capacity (int): Maximum capacity of the backpack.
        weights (list[int]): List of weights of the gold bars.

    Returns:
        int: Maximum total weight of gold that can be carried.
    """
    # initialize DP table with item count rows, and capacity+1 columns
    value: list[list[int]] = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]

    # for each gold bar
    for i in range(1, len(weights) + 1):
        gold_bar: int = weights[i - 1]

        # for each capacity up to the max
        for w in range(capacity + 1):
            # default: value if we don't take the current bar
            value[i][w] = value[i - 1][w]

            # consider taking the bar if it fits
            if gold_bar <= w:
                with_bar: int = value[i - 1][w - gold_bar] + gold_bar
                value[i][w] = max(with_bar, value[i][w])

    return value[-1][-1]



    



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
