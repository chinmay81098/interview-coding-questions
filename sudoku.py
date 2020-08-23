import time

game = [[0,0,3,0,0,0,0,0,4],
        [6,0,0,7,0,0,0,8,0],
        [7,0,0,0,6,0,2,0,0],
        [0,0,7,0,0,0,0,0,2],
        [0,4,0,1,5,2,0,9,0],
        [2,0,0,0,0,0,3,0,0],
        [0,0,9,0,3,0,0,0,8],
        [0,2,0,0,0,5,0,0,3],
        [8,0,0,0,0,0,1,0,0]]

BB = [[0 for j in range(9)] for i in range(9)]
table = {1:9,2:9,3:9,4:9,5:9,6:9,7:9,8:9,9:9}
for i in range(9):
    for j in range(9):
        if game[i][j] != 0:
            table[game[i][j]] -=1

def not_valid(game,i,j,k):
    if k in game[i]:
        return True
    for b in range(9):
        if game[b][j] == k:
            return True
    if i <3:
        if j<3:
            a,b = 0,0
        elif j <6:
            a,b = 0,3
        elif j<9:
            a,b = 0,6
    elif i <6:
        if j<3:
            a,b = 3,0
        elif j <6:
            a,b = 3,3
        elif j<9:
            a,b = 3,6
    elif i <9:
        if j<3:
            a,b = 6,0
        elif j <6:
            a,b = 6,3
        elif j<9:
            a,b = 6,6

    for x in range(a,a+3):
        for y in range(b,b+3):
            if game[x][y] == k:
                return True
    return False


def solve(game,N):
    if N == 0:
        return True
    for i in range(9):
        for j in range(9):
            if game[i][j] == 0:
                    if not_valid(game,i,j,k):
                        continue
                    game[i][j] = k
                    if solve(game,N-1):
                        return True
                    game[i][j] = 0
        return False


for r in range(9):
    for c in range(9):
        print(BB[r][c],end=' ')
    print()


