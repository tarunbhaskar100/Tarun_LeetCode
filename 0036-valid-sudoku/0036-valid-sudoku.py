class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_sudo(l):
            l.sort()
            set_su = list(set(l))
            set_su.sort()
            # print(set_su , l[-1*(len(set_su)):])
            if set_su == l[-1*(len(set_su)):]:
                return True
            else:
                return False
            
        import numpy as np
        su = np.array(board)
        for i in range(9):
            if check_sudo(list(su[i])) and check_sudo(list(su[:,i])) and check_sudo(list(su[(i//3)*3:((i//3)*3)+3,(i%3)*3:((i%3)*3)+3].flatten())):
                pass
            else:
                return False
        return True
                