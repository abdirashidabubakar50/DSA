"""
Two Sum problem. Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to taraget

You may assume each input would have exactly one solution and you not use teh same element twice

The answer can be in any order
"""

# Brute Force approach. Time Complexity O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j
        # Return an Empty list if no solution is found
        return []



# One-Pass Hash Table
"""
While iterating and iterating and inserting elements into the hash table check if current
element's complement already exists in the hash table. If it exits, we have found a solution
and return the indices
"""
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :target: int
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty array if no solution found
        return []
nums = [1, 3, 4, 5, 8, 9]
target = 14
solution1 = Solution()
result1 = solution1.twoSum(nums, target)
print("brute Force Result: ", result1)

solution2 = Solution2()
result2 = solution2.twoSum(nums, target)
print("hash map result: ", result2)


