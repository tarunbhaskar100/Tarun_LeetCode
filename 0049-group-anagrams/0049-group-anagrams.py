class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        d = []
        dup = strs.copy()
        for i,n in enumerate(dup):
            n = list(n)
            n.sort()
            n=''.join(n)
            if n not in d:
                d.append(n)
                a.append([strs[i]])
            else:
                a[d.index(n)].append(strs[i])
        return a
            
            