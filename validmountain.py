class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        peak = max(arr)
        peak_index = arr.index(peak)
        if peak_index == 0 or peak == arr[-1]:
            return False
        else:
            for i in range(peak_index-1):
                if arr[i] < arr[i+1]:
                    continue
                else:
                    return False
            for i in range(peak_index, len(arr)-1):
                if arr[i] > arr[i+1]:
                    continue
                else:
                    return False
        return True            