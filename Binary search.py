"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            
            midpoint = (first + last) // 2
            
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                first = midpoint + 1
            elif nums[midpoint] > target:
                last = midpoint - 1
        
        return -1