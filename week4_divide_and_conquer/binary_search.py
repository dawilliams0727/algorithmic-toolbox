def binary_search(keys: list[int], query: int) -> int:
    """
    Performs binary search to find the index of a query value in a sorted list.

    Args:
        keys (list[int]): A sorted list of integers.
        query (int): The integer value to search for.

    Returns:
        int: The index of the query if found, otherwise -1.
    """
    #print(f"Searching for {query} in \n{keys}")
    left: int = 0
    right: int = len(keys) - 1

    # check leftmost and rightmost elements first
    if query == keys[left]:
        return 0
    if query == keys[right]:
        return right

    # standard binary search
    while left <= right:
        mid: int = (left + right) // 2
        if keys[mid] == query:
            return mid
        elif query > keys[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
