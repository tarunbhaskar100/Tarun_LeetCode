class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        b = 0
        s = 1
        while s < len(prices):
            if prices[b] > prices[s]:
                b = s
            else:
                out = max( out ,  prices[s] - prices[b] )
            s += 1
        return out