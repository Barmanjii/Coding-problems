from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-closest-number-to-zero/description/
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest):
                closest = num

        if abs(closest) in nums and closest < 0:
            return abs(closest)
        else:
            return abs(closest)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        # https://leetcode.com/problems/merge-strings-alternately/description/
        new = ""
        max_length = len(word1) + len(word2)
        for i in range(max_length):
            if i < len(word1):
                new += word1[i]
            if i < len(word2):
                new += word2[i]
        return new

    def romanToInt(self, s: str) -> int:
        # https://leetcode.com/problems/roman-to-integer/
        roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                          'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        resultant = 0
        i = 0
        n = len(s)
        while i < n:
            if i < n-1 and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                resultant += roman_numerals[s[i+1]] - roman_numerals[s[i]]
                i += 2
            else:
                resultant += roman_numerals[s[i]]
                i += 1
        return resultant

    def hasDuplicate(self, nums: List[int]) -> bool:
        # https://neetcode.io/problems/duplicate-integer
        unique_set = set()

        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
            else:
                return True
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        # https://neetcode.io/problems/is-anagram
        # An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

        # Base Condition
        if len(s) != len(t):
            return False

        number_of_occurence = {}
        for i in s:
            if i not in number_of_occurence:
                number_of_occurence[i] = 1
            else:
                number_of_occurence[i] += 1

        for j in t:
            if j not in number_of_occurence:
                return False
            else:
                number_of_occurence[j] -= 1
                if number_of_occurence[j] == 0:
                    del number_of_occurence[j]

        if not number_of_occurence:
            return True

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # https://neetcode.io/problems/two-integer-sum
        for i in range(len(nums)):
            for j in range(i):
                if i != j and nums[i] + nums[j] == target:
                    return [j,i]
                    
            


solution = Solution()

print(solution.twoSum(nums = [5,5], target = 10))
