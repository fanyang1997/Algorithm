import time
from functools import lru_cache
import plotly.graph_objects as go
import numpy as np
from typing import Any, Dict, List, Tuple


def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)




def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time cost: {}".format(end - start))
        return result

    return wrapper

# fib_test = timeit(fib_test)
# fib_test = wrapper
# fib with memorization
memo = {}

# fib_memo = timeit(fib_memo)
# fib_memo = wrapper
#

def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    else:
        if n not in memo:
            memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo[n]


@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib_lru(n - 1) + fib_lru(n - 2)


def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    else:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def fib_dp_opt(n: int) -> int:
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


# leetcode 53 - https://leetcode.com/problems/maximum-subarray/
def max_subarray(nums: List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i] = max(dp[i - 1] + nums[i], nums[i])
    len_nums = len(nums)
    if len_nums == 1:
        return nums[0]
    dp = [0] * len_nums
    dp[0] = nums[0]
    for i in range(1, len_nums):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    return max(dp)


# leetcode 322 - https://leetcode.com/problems/coin-change/
# input: coins = [1, 2, 5], amount = 11 output: 3 (11 = 5 + 5 + 1)
# dp[11] = min(dp[11-1], dp[11-2], dp[11-5]) + 1
def coin_change(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            # dp[1] = min(dp[1], dp[1-1]) + 1)
            dp[i] = min(dp[i], dp[i - coin] + 1)
            # print(dp[i], dp[i-coin])
    return dp[amount] if dp[amount] != float("inf") else -1


# leetcode  392
def is_subsequence(s: str, t: str) -> bool:
    n, m = len(s), len(t)
    if n == 0:
        return True
    if m == 0:
        return False
    i, j = 0, 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == n



# vis time cost of fib n from 0 to 400
def vis_time_cost(n: int) -> None:
    x = np.arange(0, n + 1)
    y = [fib_dp_opt(i) for i in x]
    fig = go.Figure(
        data=[go.Scatter(x=x, y=y, mode="lines")],
        layout=go.Layout(title="Time cost of fib n from 0 to 400", xaxis=dict(title="n"), yaxis=dict(title="fib(n)"))
    )
    # set ylabel
    fig.update_layout(yaxis_title="fib(n) time cost (s)")
    fig.update_layout(xaxis_title="n")
    fig.show()


if __name__ == "__main__":
    # n = 400
    print('test')
    # fib_test = timeit(fib_test)
    # @timeit
    # def fib_test():
    #     fib(n)

    @timeit
    def fib_test_memo():
        fib_memo(n)
    # fib_test_momo = timeit(fib_test_memo)
    #
    # @timeit
    # def fib_dp_test():
    #     fib_dp(n)
    #
    # @timeit
    # def fib_test_lru():
    #     fib_lru(n)
    #
    # @timeit
    # def fib_dp_opt_test():
    #     fib_dp_opt(n)
    #
    # fib_test_memo()
    # fib_test_lru()
    # fib_dp_test()
    # fib_dp_opt_test()
    fib_memo(10)
    # fib_memo = timeit(fib_memo)
    # vis_time_cost(1000)
    # test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(max_subarray(test_array))
    # coins = [2]
    # amount = 11
    # print(coin_change(coins, amount))
    # s = "abc"
    # t = "ahbgdc"
    # print(is_subsequence(s, t))
