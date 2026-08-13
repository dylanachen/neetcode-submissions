class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the minimum k will always be a value from piles
        # the maximum k will always be ceil(sum(piles) / h)
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = l + ((r - l) // 2)

            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(float(pile) / k)
            
            if time_to_eat <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1
        
        return min_k
