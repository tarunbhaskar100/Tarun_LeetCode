class Solution:
    def arrangeCoins(self, n: int) -> int:
        out = 0
        count = 1
        while n >= count:
            n -= count
            count += 1
            out += 1
        return out 
            
        