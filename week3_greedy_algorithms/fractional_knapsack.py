from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # zip the values and weights together and store in list
    # sort list by cost / weight
    items = list(zip(values, weights))
    items.sort(key=lambda x: 0 if x[1] == 0 else x[0] / x[1], reverse = True)
    # iterate through list and add as much of the most valuable item as possible
    # if item is too large, take a fraction that fills up the knapsack
    while capacity > 0 and items:
        # look at highest value item
        current_item = items[0]
        # if weight of item is less than capacity, take all of it
        if current_item[1] <= capacity:
            # add value of item to total value
            # subtract weight of item from capacity
            # remove item from list
            value += current_item[0]
            capacity -= current_item[1]
            items.pop(0)
        else: # if weight of item is more than capacity, take a fraction of it
            # add value of item to total value
            # set capacity to zero (knapsack is full)
            # remove item from list
            max_fraction = capacity / current_item[1]
            value += max_fraction * current_item[0]
            capacity = 0
            items.pop(0)
        
        

    return round(value,4)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
