from typing import List


class Solution:
    # https://leetcode.com/problems/summary-ranges/description/
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []

        output = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if start == nums[i]:  # handle the last element\
                output.append(f"{start}")
            else:
                output.append(f"{start} -> {nums[i]}")
            i += 1
        return output


solution = Solution()

print(solution.summaryRanges(
    nums=[0, 1, 2, 4, 5, 7]))
