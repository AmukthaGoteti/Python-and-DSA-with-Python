"""
    Problem Statement:
        Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
        return the minimum integer common to both arrays. 
        If there is no common integer amongst nums1 and nums2, return -1.
        Note that an integer is said to be common to nums1 and nums2 
        if both arrays have at least one occurrence of that integer.
    
    Difficulty: Easy
    URL: https://leetcode.com/problems/minimum-common-value/
"""

n, m = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

minimum_common_value = -1

for i in range(n):
    for j in range(m):
        if nums1[i] == nums2[j]:
            if minimum_common_value == -1 or nums1[i] < minimum_common_value:
                minimum_common_value = nums1[i]

print(minimum_common_value)