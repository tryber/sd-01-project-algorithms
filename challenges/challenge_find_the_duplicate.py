from typing import List


def find_duplicate(nums: List) -> int:
    if len(nums) == 0:
        return -1
    nums.sort()
    h_index = len(nums) - 1
    lower_index, higher_index = 1, h_index

    while lower_index < higher_index:
        middle_index = (lower_index + higher_index) // 2
        less = 0
        equal = 0

        for num in nums:
            if num < middle_index:
                less += 1
            elif num == middle_index:
                equal += 1

        if equal > 1:
            return middle_index
        else:
            lower_index = middle_index + 1

    return lower_index
