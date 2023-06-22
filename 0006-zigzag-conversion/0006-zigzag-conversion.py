class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 or len(s)==1:
            return s
        st = ''
        for i in range(numRows):
            if (i == 0) or (i == numRows-1):
                st = st+s[i::(numRows - 1)*2]
                
            else:
                a=''
                inp1,inp2 = s[i::(numRows - 1)*2],s[(numRows - 1)*2 - i::(numRows - 1)*2]
                out1 = ''.join(map(''.join, zip(inp1, inp2)))
                
                if len(inp1) != len(inp2):
                    a=inp1[-1]
                st = st+out1+a
                    
        return st