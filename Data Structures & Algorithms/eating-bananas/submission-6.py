class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the minimum k will always be 1
        # the maximum k will always be max(piles)
        # binary search through the space and find if an eating rate can finish the piles in <= h time, keeping track of min_k
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = l + ((r - l) // 2)
    
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / k)
            
            if time_to_eat <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1
        
        return min_k
