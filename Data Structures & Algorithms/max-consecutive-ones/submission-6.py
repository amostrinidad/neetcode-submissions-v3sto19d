class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        10/3/26
        count = 0
        newMax = 0

        for num in nums:
            if num == 1:
                count += 1
                newMax = max(newMax, count)
            else:
                count = 0
        return newMax
                