class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        rate = 1
        while l<r:
            mid = (l+r) // 2

            rate = piles[l]/mid

            if rate <= h:
                res = int(min(res,rate))
            
            if rate < h:
                r = mid  - 1
            else:
                l = mid + 1
            

        print(res)
        return res


