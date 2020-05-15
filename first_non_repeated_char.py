s = input()
d = {}
for i in s:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1
for i in list(d.keys()):
    if d[i] == 1:
        print("First non repeating character is: {}".format(i))
        break