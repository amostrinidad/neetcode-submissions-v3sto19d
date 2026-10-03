class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 10/3/26
        length = len(arr)
        temp = [0] * length

        rightMax = -1
        currMax = 0


        for i in range(length - 1, -1, -1):
            temp[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return temp
