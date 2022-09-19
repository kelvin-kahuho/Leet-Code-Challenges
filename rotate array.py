"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]

#BEST PRACTICE
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k, tempNum = k % len(nums), nums.copy()
        for idx in range(len(nums)):
            insert = (idx + k) % len(nums)
            nums[insert] = tempNum[idx]
        
        return()