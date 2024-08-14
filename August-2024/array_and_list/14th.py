from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # https://neetcode.io/problems/top-k-elements-in-list
        if len(nums) == 1 and k == 1:
            return nums

        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, value in count.items():
            freq[value].append(key)
        res = []
        for current in range(len(freq)-1, 0, -1):
            for i in freq[current]:
                res.append(i)
                if (len(res)) == k:
                    return sorted(res)


solution = Solution()

print(solution.topKFrequent(
    nums=[1, 2, 2, 3, 3, 3], k=2))
