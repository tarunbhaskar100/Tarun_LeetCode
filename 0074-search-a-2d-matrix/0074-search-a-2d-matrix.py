class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target < i[0]:
                break 
            if target in i:
                return True
        return False