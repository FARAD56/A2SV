class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        a = len(arr) - 1
        idx = 0
        for i in range(len(arr) - 2, 0, -1):
            if arr[i] > arr[i+1]:
                idx = i
                break

        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[idx] and arr[i-1] != arr[i]:
                arr[idx], arr[i] = arr[i], arr[idx]
                break

        return arr
