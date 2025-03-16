def compute_operations(n):
    """
        Find the minimum numberof operations needed
        to get a positive integer n from 1 by using only
        three operations: add 1, multiply by 2, and mul
        tiply by 3
    """
    # what is the smallest subproblem? 
    """ What is minimum number of operations to get to number n-1?"""
    if n == 1:
        return [1]
    dp = [0,0]
    num = [-1,0]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + 1)
        num.append(i - 1)
        if i % 2 == 0 and dp[i] > dp[i//2]+1:
            dp[i] = dp[i // 2] + 1
            num[i] = i // 2
        if i % 3 == 0 and dp[i] > dp[i//3]+1:
            dp[i] = dp[i // 3] + 1
            num[i] = i // 3

    curr = num[n]
    path = [curr]
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
