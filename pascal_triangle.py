# Pascal's Triangle
#       1
#      1 1
#     1 2 1 
#    1 3 3 1
#   1 4 6 4 1
#  1 5 10 10 5 1
#It is mostly used for calculating large nCr values

n = int(input())
r = int(input())
pT = [[1 for j in range(i+1)] for i in range(n+1)]
for i in range(1,n):
    for j in range(i):
        pT[i+1][j+1] = pT[i][j] + pT[i][j+1]
print(pT[n][r])