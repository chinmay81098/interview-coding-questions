def printMatrix(r,c,mtx):
    for i in range(r):
        for j in range(c):
            print(mtx[i][j],end=" ")
        print()

def transpose(r,c,mtx):
    for i in range(c):
        for j in range(r):
            print(mtx[j][i],end=" ")
        print()

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
mtx = []
for i in range(r):
    row = list(map(int,input().split()))
    mtx.append(row)
print("\n")
#printMatrix(r,c,mtx)
print("Transpose of input matrix is: ")
transpose(r,c,mtx)