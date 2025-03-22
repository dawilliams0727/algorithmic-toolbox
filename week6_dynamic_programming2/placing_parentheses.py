def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset: str) -> int:
    """
    Parenthesizes an arithmetic expression to maximize its value.

    Given a string of digits and binary operators ('+', '-', '*'), computes the maximum
    value achievable by adding parentheses to the expression.

    Args:
        dataset (str): The input arithmetic expression (e.g. "1+5*2-3").

    Returns:
        int: The maximum value obtainable by parenthesizing the expression.
    """
    # split dataset into digits and operands
    digits: list[int] = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    operands: list[str] = [dataset[i] for i in range(1, len(dataset), 2)]

    n: int = len(digits)

    # min and max table to store values for E(i,j)
    min_table: list[list[float]] = [[float("inf")] * n for _ in range(n)]
    max_table: list[list[float]] = [[float("-inf")] * n for _ in range(n)]

    # initialize diagonals
    for i in range(n):
        min_table[i][i] = digits[i]
        max_table[i][i] = digits[i]

    def evaluate(a: int, b: int, op: str) -> int:
        """Evaluates a binary operation between two integers."""
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            raise ValueError(f"Unsupported operator: {op}")

    def MinAndMax(i: int, j: int) -> tuple[int, int]:
        """
        Calculates the minimum and maximum value for subexpression from i to j.

        Args:
            i (int): Start index.
            j (int): End index.

        Returns:
            tuple[int, int]: Minimum and maximum value for the expression range.
        """
        min_value: float = float("inf")
        max_value: float = float("-inf")

        for k in range(i, j):
            a = evaluate(max_table[i][k], max_table[k + 1][j], operands[k])
            b = evaluate(min_table[i][k], min_table[k + 1][j], operands[k])
            c = evaluate(max_table[i][k], min_table[k + 1][j], operands[k])
            d = evaluate(min_table[i][k], max_table[k + 1][j], operands[k])

            min_value = min(min_value, a, b, c, d)
            max_value = max(max_value, a, b, c, d)

        return int(min_value), int(max_value)

    # fill DP tables
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_table[i][j], max_table[i][j] = MinAndMax(i, j)

    return max_table[0][n - 1]



if __name__ == "__main__":
    print(maximum_value(input()))
