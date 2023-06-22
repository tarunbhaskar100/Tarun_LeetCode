class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        import numpy as np
        matrix[:] = matrix[::-1] 
        # print(np.array(matrix).T)
        matrix[:] = np.array(matrix).T.tolist()