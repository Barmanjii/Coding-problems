from collections import defaultdict
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # https://leetcode.com/problems/is-subsequence/description/
        S = len(s)
        T = len(t)

        j = 0

        # Base conditions
        if s == '':
            return True

        if S > T:
            return False

        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # https://neetcode.io/problems/anagram-groupsc
        res = defaultdict(list)

        for current_string in strs:
            count = [0] * 26
            for char in current_string:
                count[ord(char)-ord("a")] += 1

            res[tuple(count)].append(current_string)

        return res.values()


solution = Solution()

print(solution.groupAnagrams(
    strs=["act", "pots", "tops", "cat", "stop", "hat"]))
