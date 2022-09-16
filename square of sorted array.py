"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

from math import sqrt
import numpy as np
from bisect import insort
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
            squared_numbers = [number ** 2 for number in nums]
            squared_numbers = np.sort(squared_numbers)
            return squared_numbers

#BEST PRACTICE

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        res = []
        while(l<r):
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r]*nums[r])
                r-=1
        if l==r:
            res.append(nums[r]*nums[r])
        return res[::-1]