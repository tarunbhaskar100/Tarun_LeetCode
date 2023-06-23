class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p = int(a,2)+int(b,2)
        out = ''
        while p not in [1,0]:
            p, r = p//2,p%2
            print(p,r)
            out = str(r)+out
        return str(p)+out