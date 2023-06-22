class Solution:
    def maxArea(self, height: List[int]) -> int:
        pl = 0
        pr = len(height) - 1
        def next_pr(pl,pr):
            for i in range(pr-1,pl,-1):
                if height[i]>height[pr]:
                    pr = i
                    break
            return pr
        def next_pl(pl,pr):
            for i in range(pl+1,pr):
                if height[i]>height[pl]:
                    pl = i
                    break
            return pl
        def water_vol(pl,pr):
            return(pr-pl)*min(height[pr],height[pl])
        s = water_vol(pl,pr)
        while pl < pr:

            if height[pl] > height[pr]:
                n = pr
                pr = next_pr(pl,pr)
                if n == pr:
                    break
            else:
                n = pl
                pl = next_pl(pl,pr)
                if n == pl:
                    break
            if s < water_vol(pl,pr):
                s = water_vol(pl,pr)
        return s
