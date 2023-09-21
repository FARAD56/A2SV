class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array = [0]*(rowIndex+1) 
        array[-1] = 1

        def comp(array):
            if array[0] == 1:
                return array

            for i in range(rowIndex):
                array[i] = array[i] + array[i+1]

            return comp(array)

        return comp(array)
