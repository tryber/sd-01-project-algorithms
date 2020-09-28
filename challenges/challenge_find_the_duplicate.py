def find_duplicate(nums):
    nums.sort()
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False


nums = [1, 2, 2, 3, 4]
print(find_duplicate(nums))
