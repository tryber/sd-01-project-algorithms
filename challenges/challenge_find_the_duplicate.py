from typing import List


def find_duplicate(nums: List) -> int:
    nums.sort()
    h_index = len(nums) - 1
    lower_index, higher_index = 1, h_index

    while lower_index < higher_index:
        middle_index = (lower_index + higher_index) // 2
        less, equal = 0, 0

        for num in nums:
            if num < middle_index:
                less += 1
            elif num == middle_index:
                equal += 1

        if equal > 1:
            return middle_index

        if less >= middle_index:
            higher_index = middle_index - 1
        else:
            lower_index = middle_index + 1

    return lower_index
