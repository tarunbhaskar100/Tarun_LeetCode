class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def backup(x,y):
            if x > len(triangle)-1 or y > len(triangle[-1])-1:
                return 0
            if (x,y) in dp.keys():
                return dp[(x,y)]
            dp[(x,y)] = min(triangle[x][y]+backup(x+1,y),triangle[x][y]+backup(x+1,y+1))
            return dp[(x,y)]
        return backup(0,0)