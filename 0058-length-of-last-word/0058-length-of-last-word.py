class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        for i in range(1,len(s)+1):
            if s[-i] != "":
                break
        return len(s[-i])