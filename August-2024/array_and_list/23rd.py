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

    # https://neetcode.io/problems/string-encode-and-decode
    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        self.decode(s=result)
        return result

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            n = int(s[i:j])

            res.append(s[j+1:j+1+n])
            i = n+j+1
        print(res)
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # https://neetcode.io/problems/products-of-array-discluding-self
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res


solution = Solution()

print(solution.productExceptSelf(
    nums=[1, 2, 3, 4]))
