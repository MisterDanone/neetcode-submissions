class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

       
        
        for i in board:
            arr = []
            for num in i:
                if num in "123456789":
                    arr.append(num)
            if len(arr) != len(set(arr)):
                return False

        ''' Проверка колонок и строк'''
        for i in range(9):
            collumn = []
            for j in board:
                collumn.append(j[i])
            c = collumn.count('.') - 1
            if len(set(collumn)) + c != len(collumn):
                return False

        '''sub-boxes check'''

        for z in range(3):
            for n in range(3):
                arr = []
                for x in range(0 + 3*n, 3 + 3*n):
                    for y in range(0 + 3*z, 3 + 3*z):
                        if board[x][y] in "123456789":
                            arr.append(board[x][y])
                if len(arr) != len(set(arr)):
                    return False

            
        return True
        