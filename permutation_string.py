def permute(s,i,n):
    if i == n -1 :
        print("".join(s))
    else:
        for j in range(i,n):
            s[i],s[j] = s[j],s[i]
            permute(s,i+1,n)
            s[i],s[j] = s[j],s[i]
s = input()
s = list(s)
n = len(s)
print("\nPermutaion of the given string")
permute(s,0,n)