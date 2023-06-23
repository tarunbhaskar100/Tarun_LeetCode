class Solution:
    def isNumber(self, s: str) -> bool:
        if "e" in s:
            s = s.split("e")
            
        elif "E" in s:
            s = s.split("E")
        else:
            if ("inf" in s) or ("Infinity" in s):
                return False
            try:
                t = float(s)
                return True
            except:
                return False
        if (s[0] == "") or (s[-1] == "") or len(s) > 2:
            return False
        try:
            # print(s)
            t = float(s[0])
            if int(s[-1]) -float(s[-1]) == 0.0 :
                return True
            else:
                return False
        except:
            return False
        