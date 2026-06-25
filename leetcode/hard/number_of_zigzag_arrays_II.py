"""
    Problem Statement:
        You are given three integers n, l, and r.
        A ZigZag array of length n is defined as follows:
        Each element lies in the range [l, r].
        No two adjacent elements are equal.
        No three consecutive elements form a strictly increasing or strictly decreasing sequence.
        Return the total number of valid ZigZag arrays.
        Since the answer may be large, return it modulo 109 + 7.
        A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
        A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).
    
    Difficulty: Hard
    URL: https://leetcode.com/problems/number-of-zigzag-arrays-ii/description/?envType=daily-question&envId=2026-06-24
"""
    
MOD = 10**9 + 7


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m % MOD
        if m == 1:
            return 0

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        # Length = 2
        for x in range(1, m + 1):
            up[x] = x - 1
            down[x] = m - x

        for _ in range(3, n + 1):
            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            prefix = 0
            for x in range(1, m + 1):
                new_up[x] = prefix
                prefix = (prefix + down[x]) % MOD

            suffix = 0
            for x in range(m, 0, -1):
                new_down[x] = suffix
                suffix = (suffix + up[x]) % MOD

            up = new_up
            down = new_down

        ans = 0
        for x in range(1, m + 1):
            ans = (ans + up[x] + down[x]) % MOD

        return ans


if __name__ == "__main__":
    n, l, r = map(int, input("Enter n, l, r: ").split())

    sol = Solution()
    print(sol.zigZagArrays(n, l, r))