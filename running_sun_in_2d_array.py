"""
1480. Running Sum of 1d Array
Easy
7.3K
325
Companies
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
Accepted
1.6M
Submissions
1.9M
Acceptance Rate
86.7%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (89)
Related Topics
Copyright ©️ 2023 LeetCode All rights reserved
"""


nums = [1,2,3,4,5]


i = 1
end = len(nums)

while (i < end):
  nums[i] = nums[i-1] + nums[i]
  print('Updated value of nums[i]:', nums[i])
  i = i + 1
        

print(nums)