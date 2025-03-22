from sys import stdin


def maximum_gold(capacity, weights):
    """
        Given a set of gold bars of various weights and
        a backpack that can hold at most W pounds,
        place as much gold as possible into the backpack.
    """
    # initialize DP table with item count rows, and capacity length columns
    value = [[0]*(capacity+1) for _ in range(len(weights)+1)]
    # for each gold bar
    for i in range(1,len(weights)+1):
        goldBar = weights[i-1]
        # for each smaller capacity up to target capacity
        for w in range(capacity+1):
            # if the weight of goldBar is at most weight of backpack
            # set value of backpack as if gold bar isn't used
            value[i][w] = value[i-1][w]
            if goldBar <= w:
                # weight if gold bar is used
                withBar = value[i-1][w-goldBar] + goldBar
                # value[goldBar][w] is the larger of the two
                value[i][w] = max(withBar, value[i][w])

    return value[-1][-1]


    



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
