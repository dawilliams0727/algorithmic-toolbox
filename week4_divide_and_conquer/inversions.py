from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def inversions(a: list[int]) -> int:
    """
    Counts the number of inversions in the list using a modified merge sort.

    Args:
        a (list[int]): The input list.

    Returns:
        int: The number of inversions in the list.
    """
    def merge_sort(arr: list[int]) -> tuple[list[int], int]:
        if len(arr) <= 1:
            return arr, 0

        mid: int = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge_and_count(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge_and_count(left: list[int], right: list[int]) -> tuple[list[int], int]:
        merged: list[int] = []
        i = j = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i  # All remaining elements in left are inversions
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_inversions = merge_sort(a)
    return total_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions(elements))
