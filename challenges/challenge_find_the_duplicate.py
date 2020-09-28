def find_duplicate(nums):
    for num in nums:
        if nums.count(num) > 1:
            return num


nums = [1, 2, 3, 3, 4]
print(find_duplicate(nums))
