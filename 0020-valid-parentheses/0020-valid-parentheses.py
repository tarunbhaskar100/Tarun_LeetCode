class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 == 1:
            return False
        l = ['']
        d ={'(':')','[':']','{':'}','':''}
        for i in s:
            try:
                if i == d[l[-1]]:
                    l = l[:-1]
                else:
                    l.append(i)
            except:
                return False
        if len(l) > 1:
            return False
        return True
            
        