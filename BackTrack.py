def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]:
            return False

    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]:
            return False

    return True

def solve(board,row,n):
    if row >=n:
        print_solution(board)
        return True

    success = False

    for col in range(n):
        #print(col)
        if is_safe(board,row,col,n):
            board[row][col]=1
            success=solve(board,row+1,n) or success
            board[row][col]=0 #backtrack
    return success

n=4
board=[[0]*n for _ in range(n)]
print("solution to ",n,"Queen problem")
solve(board,0,n)
