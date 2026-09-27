def quick_sort(array: list) -> list:
    if len(array) <= 1: return array

    pivot = array[len(array) // 2]

    left_side = [x for x in array if x < pivot]
    right_side = [x for x in array if x > pivot]
    middle = [x for x in array if x == pivot]

    return quick_sort(left_side) + middle + quick_sort(right_side)

