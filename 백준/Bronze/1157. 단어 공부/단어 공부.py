# 단어 공부

word = input().upper()
w = list(set(word))
# print(w)

c = []

for x in w:
    # print(word.count(x))
    c.append(word.count(x))


if(c.count(max(c))>1):
    print("?")
else:
    print(w[c.index(max(c))])

