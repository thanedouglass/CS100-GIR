# DO NOT MODIFY THE FUNCTION HEADER
# This is autograded. If the autograder cannot run your code, you will get a zero.
# Your final submission should not contain any print statements as this might cause the autograder to crash.
def solution(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False 
