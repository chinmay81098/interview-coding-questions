def squareRoot(f,l,n):
        m = (f+l)/2
        sq = m*m
        if sq == n or abs(sq - n)< 0.0001:
            print("Square root: {0:.5f}".format(m))
        elif sq < n:
            squareRoot(m,l,n)
        elif sq > n:
            squareRoot(f,m,n)
def find_square_root(n):
    curr = 1
    found = False
    while not found:
        mul = curr*curr
        if mul == n:
            print("Square root: {}".format(curr))
            found = True
        elif mul > n:
            squareRoot(curr-1,curr,n)
            found = True
        curr += 1

n = float(input("Enter a number :"))
find_square_root(n)
