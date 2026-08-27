class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        lower = n - 1
        upper = n
        temp = -1

        for i in range(n - 2, -1, -1):
            curr = arr[i]
            maxRight = max(temp, max(arr[lower:upper]))
            arr[i] = maxRight
            temp = curr
            lower -= 1

        arr[n - 1] = -1

        return arr