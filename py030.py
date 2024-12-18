for i in range(9):
            for j in range(len(board)):
                for k in range(len(board)):
                    if(board[i][j]==board[i][k] or board[j][i]==board[k][i] or board[3*(i//3)+j//3][3*(i%3)+j%3]==board[3*(i//3)+k//3][3*(i%3)+k%3])and(j != k):
                        return True
        return False