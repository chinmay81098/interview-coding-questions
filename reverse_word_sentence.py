def reverse(word):
    w = []
    for i in range(len(word)-1,-1,-1):
        w.append(word[i])
    return "".join(w)
def new_sen(sen):
    r_sen = []
    for word in sen.split(" "):
        r_sen.append(reverse(word))
    return " ".join(r_sen)
sen = input()
print(new_sen(sen))