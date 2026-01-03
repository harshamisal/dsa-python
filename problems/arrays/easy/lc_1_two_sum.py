"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy
Topic: Arrays + Hashing

Problem Statement:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Approach:
- Use a hash map to store seen numbers
- For each number, check if (target - num) exists

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:

    # # brute force
    # def twoSum(nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    
    # hashmap
    def twoSum(self, nums, target):
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i

obj = Solution()

print(obj.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(obj.twoSum([3, 2, 4], 6))      # [1, 2]
print(obj.twoSum([3, 3], 6))         # [0, 1]