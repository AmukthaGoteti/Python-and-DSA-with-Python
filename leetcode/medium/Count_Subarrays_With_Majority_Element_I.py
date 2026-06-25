"""
    Problem Statement:
        Given a string text, you want to use the characters of text to 
        form as many instances of the word "balloon" as possible.
        You can use each character in text at most once. 
        Return the maximum number of instances that can be formed.
    
    Difficulty: Medium
    URL: https://leetcode.com/problems/count-subarrays-with-majority-element-i/?envType=daily-question&envId=2026-06-25
"""

class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        # Convert to +1 (target) and -1 (others)
        arr = [1 if x == target else -1 for x in nums]

        offset = n + 1
        size = 2 * n + 5
        bit = [0] * size

        def update(i, val):
            while i < size:
                bit[i] += val
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        prefix = 0
        ans = 0

        # Empty prefix sum = 0
        update(offset, 1)

        for x in arr:
            prefix += x
            idx = prefix + offset

            # Count previous prefix sums < current prefix sum
            ans += query(idx - 1)

            update(idx, 1)

        return ans


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    target = int(input("Enter target: "))

    sol = Solution()
    print("Number of subarrays:", sol.countMajoritySubarrays(nums, target))