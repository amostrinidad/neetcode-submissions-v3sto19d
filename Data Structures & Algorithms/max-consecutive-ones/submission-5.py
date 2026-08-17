class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSeq = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                maxSeq = max(maxSeq, count)
            else:
                count = 0
        return maxSeq

    # Version 2:
    # Compare count to maxSeq through every iteration and update for every 1
    # This eliminates the need to run another max comparison in the end
    # Just loop through once, and compare once, and return maxSeq variable