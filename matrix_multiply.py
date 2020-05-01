def product_of_mtx(r1,c1,r2,c2):
    mtx3 = []
    if c1 != r2:
        return "Product not possible"
    else:
        for i in range(r1):
            row = []
            for k in range(c2):
                s = 0
                for j in range(c1):
                    s = s+ mtx1[i][j]*mtx2[j][k]
                row.append(s)
            mtx3.append(row)
    return mtx3

r1 = int(input("Enter rows of first: "))
c1 = int(input("Enter columns of first: "))
mtx1 = []
for i in range(r1):
    row = list(map(int,input().split()))
    mtx1.append(row)
print("\n")
r2 = int(input("Enter rows of second: "))
c2 = int(input("Enter columns of second: "))
mtx2 = []
for i in range(r2):
    row = list(map(int,input().split()))
    mtx2.append(row)
output = product_of_mtx(r1,c1,r2,c2)
print('Product of Matrices is:')
for i in range(r1):
    for j in range(c2):
        print(output[i][j],end=" ")
    print()
