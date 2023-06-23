class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mo={}
        def backup(x,y):
            if (x == n-1) and (y == m-1):
                return 1
            if (x >= n) or (y >= m):
                return 0
            if (x,y) in mo.keys():
                return mo[(x,y)]
            mo[(x,y)] = backup(x+1,y) + backup(x,y+1)
            return mo[(x,y)]
        return backup(0,0)