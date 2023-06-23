class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        if numRows == 1:
            return [1]
        else :
            out = [[1],[1,1]]
            for i in range(1,numRows-1):
                d = [1]*(i+2)
                for j in range(i):
                    d[j+1] = out[-1][j]+out[-1][j+1]
                out.append(d)
            return out[-1]