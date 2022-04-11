
    # Longest
    # Common
    # Subsequence
def longest_commen_subseq(string1, string2):
    """
    :param string1:
    :param string2:
    :return:
    """
    dp = [[0] * (len(string1) + 1) for _ in range(len(string2) + 1)]
    for i in range(len(string2)):
        for j in range(len(string1)):
            if string2[i] == string1[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]



def KMP(string, pattern):
    """
    using next array
    :param string:
    :param pattern:
    :return:
    """
    next = get_next(pattern)
    i = 0
    j = 0
    while i < len(string) and j < len(pattern):
        if j == -1 or string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(pattern):
        return i - j
    return -1

def get_next(pattern):
    """
    get next array
    :param pattern:
    :return:
    """
    next = [-1] * len(pattern)
    i = 0
    j = -1
    while i < len(pattern) - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next


test_case = {
    "abcdefgh, cd": 2,
    "ffffffff, f": 0,
}
#
# for key, value in test_case.items():
#     assert KMP(key, value) == value


get_next("abcdeabc")