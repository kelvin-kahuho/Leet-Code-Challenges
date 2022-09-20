"""
Two Sum II - Input Array Is Sorted
Medium

7675

1071

Add to List

Share
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        sum = 0
        while start != end :
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start +=1
            else:
                return start+1,end+1
#BEST PRACTICE

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l+1, r+1]
            