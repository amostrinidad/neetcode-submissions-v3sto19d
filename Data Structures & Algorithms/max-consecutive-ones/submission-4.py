class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxSeq = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxSeq = max(count, maxSeq)
                count = 0
        maxSeq = (max(count, maxSeq))
        return maxSeq