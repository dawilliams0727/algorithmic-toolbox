def edit_distance(first_string, second_string):
    # you can either remove the previous symbol, insert a space at the previous symbol, or change previous symbol
    # to get to the current symbol
    n,m = len(first_string), len(second_string)
    table = [[0]*(m+1) for _ in range(n+1)]
    #print(f"first:{first_string} second:{second_string}\nTable rows: {len(table)} \tTable Columns: {len(table[0])}\n{table}")
    
    for i in range(n+1):
        table[i][0] = i
    for j in range(m+1):
        table[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            insertion = table[i][j-1] + 1
            deletion = table[i-1][j] + 1
            isMatch = table[i-1][j-1]
            mismatch = table[i-1][j-1] + 1
            if first_string[i-1] == second_string[j-1]:
                table[i][j] = isMatch
            else:
                 table[i][j] = min(insertion, deletion, mismatch)

    def print_table():
        print("",second_string)
        for i, row in enumerate(table):
            print(f"{first_string[i]}{row}")

    return table[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
