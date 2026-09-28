class Solution:
    from math import ceil
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            mid = (l + r) // 2
            total_time = sum(math.ceil(pile / mid) for pile in piles)
            if total_time > h:
                l = mid + 1
            else:
                r = mid 
        return l