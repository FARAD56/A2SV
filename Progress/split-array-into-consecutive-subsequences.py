class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        i = 0
        ans,con = [],[]
        heapify(ans)

        def comp(ans,reserve,i,con):
            for _ in range(len(ans)):
                l,n = heappop(ans)

                if nums[i] == n+1:
                    reserve.append((l+1,n+1))
                    return reserve, True
                elif nums[i] > n+1:
                    con.append((l,n))
                else:
                    reserve.append((l,n))
            return reserve,False

        while i < len(nums):
            reserve = []
            reserve, bl = comp(ans, reserve,i,con)
        
            for tup in reserve:
                heappush(ans, tup)

            if not bl:
                heappush(ans, (1, nums[i]))

            i+=1

        print(con)
        for _ in range(len(ans)):
            top = heappop(ans)
            if top[0] < 3:
                return False
        for a in con:
            if a[0] < 3:
                return False
        return True



        
        