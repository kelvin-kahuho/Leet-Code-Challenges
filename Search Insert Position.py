"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity
"""
from bisect import insort
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for number in nums:
            if number == target:
                index = nums.index(target)
                return index
            else:
                if target not in nums:
                    bisect.insort(nums, target) 
                    index = nums.index(target)
                    return index
        return None

"""
BEST PRACTICES
"""
#i Still don't understand how the problem is solved using this method
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)                