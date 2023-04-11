"""
Challenge: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6

Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6

Output: [0,1]

Solution:

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i


"""
The twoSum function takes an array of integers nums and an integer target as input, and returns a list of indices of the two numbers that add up to target. The function uses a dictionary d to store the values of nums along with their indices.

The function then loops over the elements of nums, and for each element nums[i], it checks whether target - nums[i] is already in the dictionary d. If so, it returns the indices of the two elements that add up to target. If not, it adds nums[i] to the dictionary d along with its index.

The time complexity of this algorithm is O(n), where n is the length of the input array nums. The space complexity is also O(n), due to the use of the dictionary d.
"""






