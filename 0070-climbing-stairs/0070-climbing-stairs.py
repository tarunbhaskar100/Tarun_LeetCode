class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1,2]
        if n < 2 :
            return 1
        for i in range(2,n):
            memo.append(memo[-1]+memo[-2])
        return memo[-1]