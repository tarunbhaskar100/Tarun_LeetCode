class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 1
        st = 0
        
        if len(s) > 2:
            i = 2
            while i <= len(s):
                print(s[st:i])
                if (len(s[st:i]) == len(set(s[st:i]))):
                    if (len(s[st:i]) > out):
                    # print(s[st:i])
                        out = len(s[st:i])
                    i = i+1
                elif st > i-2:
                    i = i+1
                else:
                    st += 1
            return out
        else:
            return len(set(s))