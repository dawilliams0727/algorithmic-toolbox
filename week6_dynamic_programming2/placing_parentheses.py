def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    """
    Parenthesize an arithmetic expression to maximize its value and return the value of the expression
    """
    # split dataset into digits and operands
    digits = [int(dataset[i]) for i in range(0,len(dataset), 2)]
    operands = [dataset[i] for i in range(1, len(dataset),2)] 
    # determine n
    n = (len(dataset) + 1) // 2
    # min and max table to store values for E(i,j) of size
    min_table = [[float("inf") for _ in range(n)] for _ in range(n)]
    max_table = [[float("-inf") for _ in range(n)] for _ in range(n)]
    # initialize the main diagonals with the digits (corresponds to no need for evaluation of min or max)
    for i in range(n):
        min_table[i][i] = digits[i]
        max_table[i][i] = digits[i]
    
    # define function for calulating min and max
    def MinAndMax(i: int,j: int):
        """
        Calculate the minimum and maximum values for all possible subexpressions ranging from i to j
        """
        minValue, maxValue = float("inf"), float("-inf")
        for k in range(i, j):
            a = evaluate(max_table[i][k], max_table[k+1][j], operands[k])
            b = evaluate(min_table[i][k], min_table[k+1][j], operands[k])
            c = evaluate(max_table[i][k], min_table[k+1][j], operands[k])
            d = evaluate(min_table[i][k], max_table[k+1][j], operands[k])
            minValue = min(minValue,a,b,c,d)
            maxValue = max(maxValue,a,b,c,d)
        return (minValue, maxValue)
    
    # iterate along each diagonal, filling dp tables
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            min_table[i][j], max_table[i][j] = MinAndMax(i,j)

    return max_table[0][-1]


if __name__ == "__main__":
    print(maximum_value(input()))
