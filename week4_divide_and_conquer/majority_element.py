def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    ...
    #sort the elements
    from math import ceil
    elements.sort()
    
    # get array containing occurences of the midpoint
    def get_midpoint(array):
        left,right = 0, len(array) 
        mid = (left + right) // 2
        mid_element = array[mid]
        index = mid
        occurences = [num for num in array if num == mid_element]
        #print(index, occurences)
        return (index, occurences)
    
    # RECURSIVE
    def recursive(array):
        # base case
        if len(array) <= 1:
             return []
        # find midpoint, and call function for checking length 
        midpoint, occurences = get_midpoint(array)
        if len(occurences) >= len(array) // 2 + 1:
            return occurences
        else:
            left, right = recursive(array[:midpoint]), recursive(array[midpoint:])
            if left and right:
                if left[0] == right[0]:
                    return left.extend(right)
                else:
                    return max(left,right, key=len)
            else:
                if left and len(left) > len(array) // 2: return left
                elif right and len(right) > len(array) // 2: return right

    result = recursive(elements)       
    #print(result)
    return 1 if result else 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
