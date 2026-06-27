class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSeq = count = 0

        for num in nums:
            if num == 1:
                count += 1
                maxSeq = max(maxSeq, count)
            else:
                count = 0
        return maxSeq