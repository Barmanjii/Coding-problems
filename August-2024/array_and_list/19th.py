from typing import List


class Solution:
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # https://leetcode.com/problems/longest-common-prefix/submissions/1361691360/
        sorted_string = sorted(strs)

        first_element = sorted_string[0]
        last_element = sorted_string[-1]

        longest_prefix = ""

        for i in range(len(first_element)):
            if first_element[i] != last_element[i]:
                break

            longest_prefix = longest_prefix + first_element[i]
        return longest_prefix


solution = Solution()

print(solution.longestCommonPrefix(
    strs=["a"]))
