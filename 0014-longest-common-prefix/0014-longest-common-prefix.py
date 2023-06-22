class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        x=min(strs)
        y=max(strs)
        n=min(len(x),len(y))
        for i in range(n):
            if x[i]==y[i]:
                ans+=x[i]
            else:
                break
        return ans    