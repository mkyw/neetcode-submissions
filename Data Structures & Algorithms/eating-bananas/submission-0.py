class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        
        l = 1
        best_k = max_k
        while l <= max_k:
            m = (l + max_k) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(float(i)/m)
            if hours <= h:
                best_k = m
                max_k = m - 1
            else:
                l = m + 1
        return best_k