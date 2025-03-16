def change(money):
    # write your code here
    # start at base case where min change is easily known
    change = [0,1,2,1,1,2]
    # for each index (corresponds to change) choose the minimum result from calls change(i - 1) + 1 )
    for i in range(6, money + 1):
        one, three, four = None, None, None
        if i - 1 >= 0:
            one = change[i - 1]
        if i - 3 >= 0:
            three = change[i - 3]
        if i - 4 >= 0:
            four = change[i-4]
        change.append(min(one, three, four) + 1)
    # as well as 3 and 4. Make sure that i - coin > 0
    # return the value at change[money]
    return change[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
