def binary_search_duplicates(keys, query):
    # write your code here
    #print(f"Searching for {query} in \n{keys}")
    # check if query found on left, return index immediately
    if keys[0] == query:
        return 0
    # if neither implement classic binary search
    left, right =  0, len(keys)
    last_found = -1
    while left <= right:
        mid = (left + right) // 2
        if mid == len(keys):
            break
        # if the query is found, check if there are any more to the left
        if keys[mid] == query:
            last_found = mid
            right = mid - 1
        elif keys[mid] > query:
            right = mid - 1
        else:
            left = mid + 1
        # continue binary search until left is also the query, or until left == right

    return last_found


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_duplicates(input_keys, q), end=' ')
