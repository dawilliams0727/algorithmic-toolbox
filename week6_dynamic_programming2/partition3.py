from sys import stdin


def partition3(values):
    """
     Partition a set of integers into three subsets with
    equal sums

    Arguments:
    values -- list of integers

    Returns:
    1 if the partition is possible, 0 otherwise
    """
    # can't create three subsets of equal size if either is true
    if len(values) <= 2 or sum(values) % 3 != 0:
        return 0
    
    TARGET_SUM = sum(values) // 3
    n = len(values)
    dp = [[False for _ in range(TARGET_SUM + 1)] for _ in range(n + 1)]
    dp[0][0]= True
    for i in range(1, n + 1):
        val = values[i - 1]
        for j in range(TARGET_SUM + 1):
            dp[i][j] = dp[i-1][j]
            if j >= val:
                dp[i][j] = dp[i][j] or dp[i-1][j-val]

    if not dp[n][TARGET_SUM]:
        return 0
    
    s1 = []
    i = n
    j = TARGET_SUM

    while i > 0 and j > 0:
        if dp[i-1][j]:
            i -= 1
        else:
            val = values[i-1]
            s1.append(val)
            j -= val  
            i -= 1    
    
    remaining = values[:]
    for x in s1:
        remaining.remove(x)

    rest = sum(remaining)
    if rest < TARGET_SUM:
        return 0
    
    m = len(remaining)
    dp2 = [[False for _ in range(TARGET_SUM+1)] for _ in range(m+1)]
    dp2[0][0] = True
    for i in range(1, m+1):
        val = remaining[i-1]
        for j in range(TARGET_SUM+1):
            dp2[i][j] = dp2[i-1][j]
            if j >= val:
                dp[i][j] = dp[i][j] or dp[i-1][j-val]
                
    if not dp[m][TARGET_SUM]:
        return 0

    return 1

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
