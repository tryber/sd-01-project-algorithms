from typing import List


# def find_duplicate(nums: List) -> int:
#     new_list = sorted(nums)
#     half = len(new_list) // 2
#     answer = 0
#     for index in range(half):


def funcname(parameter_list):
    return [i for i in parameter_list if parameter_list[i] > 1]


print(funcname([1, 3, 4, 2, 2]))