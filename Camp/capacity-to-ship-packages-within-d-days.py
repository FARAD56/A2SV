class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights), sum(weights)
        min_cap = r

        while l <= r:
            mid = (l+r)//2

            curr, count = mid,0
            for weight in weights:
                if curr + weight > mid:
                    count += 1
                    curr = 0
                curr += weight

            if count > days:
                l = mid + 1
            else:
                min_cap = mid
                r = mid - 1

        return min_cap

        
        