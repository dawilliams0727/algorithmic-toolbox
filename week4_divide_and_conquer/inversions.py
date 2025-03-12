from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def inversions(a):
    def recursive(a):
        count = 0
        # base case, if len(a) <= 1 return a
        if len(a) == 1:
            return a,count
            # no inversions possible if only 0 or 1 element
        if len(a) == 2:
            if a[0] > a[1]:
                a[0], a[1] = a[1], a[0]
                count += 1
            return a, count
        # split array into two halves
        mid = len(a) // 2
        # call inversions on left and right half
        left, right = (a[:mid]), (a[mid:])
        # merge left and right halves and count additional inversion at boundary
        lc, rc = recursive(left), recursive(right)
        for i in lc[0]:
            for j in rc[0]:
                if i > j:
                    count += 1
        return merge(lc[0], rc[0]), count+lc[1]+rc[1]
    
    result = recursive(a)
    return result[1]

def merge(left, right):
    if len(left) != len(right):
        shorter, longer = min(left, right, key=len), max(left, right, key=len)
    shorter, longer = left, right
    merged = []
    i,j = 0,0
    while i < len(shorter) and j < len(longer):
        if shorter[i] < longer[j]:
            merged.append(shorter[i])
            i += 1
        else:
            merged.append(longer[j])
            j += 1

    if i == len(shorter):
        merged.extend(longer[j:])
    elif j == len(longer):
        merged.extend(shorter[i:])
    
    return merged


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions(elements))
