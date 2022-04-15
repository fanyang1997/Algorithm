from typing import List


class Solution:

    # leetcode 05
    # https://leetcode.com/problems/longest-palindromic-substring/
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        len_s = len(s)
        if len_s == 1:
            return s
        max_len = 1
        start = 0
        for i in range(len_s):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]



    # leetcode 64
    # https://leetcode.com/problems/minimum-path-sum/
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

    # leetcode 70
    # https://leetcode.com/problems/climbing-stairs/
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]





if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
    test_case_5 = {
        "babad": "bab",
        "cbbd": "bb",
        "a": "a",
        "bb": "bb"
    }
    test_case_70 = {
        1: 1,
        2: 2,
        3: 3,
        4: 5,
        5: 8,
        6: 13,
        7: 21
    }

    test_case_64 = {
        '[[1, 3, 1], [1, 5, 1], [4, 2, 1]]': 7,
        '[[1, 2, 3], [4, 5, 6]]': 12,
        '[]': 0,
        '[[1]]': 1
    }

    for k, v in test_case_64.items():
        assert s.minPathSum(eval(k)) == v

    for k, v in test_case_70.items():
        assert s.climbStairs(k) == v

    for k, v in test_case_5.items():
        assert s.longestPalindrome(k) == v