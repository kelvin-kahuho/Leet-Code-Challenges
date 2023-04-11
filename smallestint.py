"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

"""

def solution(A):
    n = len(A)
    present = [False] * (n + 1)
    for i in range(n):
        if 1 <= A[i] <= n:
            present[A[i]] = True
    for i in range(1, n + 1):
        if not present[i]:
            return i
    return n + 1
