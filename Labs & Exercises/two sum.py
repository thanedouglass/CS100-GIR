def solution(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
         complement = target - num
         if complement in num_indices:
            return [num_indices[complement], i]
         num_indices[num] = i
    return []


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums1, target1)
print(result1)
