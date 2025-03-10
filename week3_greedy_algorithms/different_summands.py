def optimal_summands(n):
    summands = []
    # write your code here
    def quadratic_solve():
        import math
        a = 1
        b = 1
        c = 2*n*-1
        return ((-1) + math.sqrt(b**2-(4*a*c)))/(2*a)
    
    k = int(quadratic_solve())
    closest_triangular = int((k*(k+1))/2)
    remainder = n - closest_triangular
    summands = [n for n in range(1,k+1)]
    summands[-1] += remainder

    #print(f"length of array: {k}\nclosest triangular:{closest_triangular}")
    #print(f"Summands sum: {sum(summands)}")
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
