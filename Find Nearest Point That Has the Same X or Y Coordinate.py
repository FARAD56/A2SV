class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        res = [x,y]
        arr = []

        count,track = 0,[]

        for item in points:
            count +=1
            if item[0] == res[0] or item[1] == res[1]:
                arr.append(item)
                track.append(count -1)

        if len(track) == 0:
            return -1

        else:
            man_list = []

            for item in arr:
                manhattan = abs(item[0] - res[0]) + abs(item[1] - res[1])
                man_list.append(manhattan)
                

            min_value = min(enumerate(man_list), key=lambda x: x[1])
            min_index = min_value[0]

            ans = track[min_index]
            return ans

    

                    
