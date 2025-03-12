from random import randint


def partition3(array, left, right):
    # write your code here
    # keep track of comparing element
    x = array[left]
    # j and k are indices of comparison regions
    j = left + 1
    k = left + 1
    for i in range(left + 1, right + 1):
        # if array[i] is less than compare
        if array[i] <= x:
            array[j], array[i] = array[i], array[j]
            # increment j (to add smaller element to smaller region)
            j += 1

    # create region where all elements == x
    for i in range(left+1, j):
        if array[i] == x:
            array[k], array[i] = array[i], array[k]
            k += 1
    # move x set to final position
    """for i in range(k,j):
        array[i-k + left], array[i] = array[i], array[i-k + left]"""
    # account for if swap zones overlap
    match_region_start = left
    match_region_end = min(j-(k-left), k)
    swap_region_start = max(j - (k - left), k)
    swap_region_end = j
    temp = array[swap_region_start:swap_region_end]
    array[swap_region_start:swap_region_end] = array[match_region_start:match_region_end]
    array[match_region_start:match_region_end] = temp
    #array[left:k], array[j-k:j] = array[j-k:j], array[left:k]
    # indices of first and last element where A[m1] == x == A[m2]
    m1,m2 = left + (swap_region_end - k), swap_region_end - 1

    return m1, m2

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    input_n = len(elements)
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
