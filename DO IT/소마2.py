letters = "i#my##me###mine"
n = 4

letters_len = len(letters)
words = letters.split("#")  # ["natural", "language", "processing"]
myList = []
word = ""

for i in range(len(letters)):
    if i == letters_len-1:  # 마지막이라면
        word += letters[i]
        myList.append(word)
        continue

    if letters[i] == "#":
        if len(word) > 0:  # "##"인 경우 고려
            myList.append(word)
            word = ""  # 초기화
        myList.append(letters[i])
    else:
        word += letters[i]  # 그냥 이렇게 했어도 됐을 것 같은...

# n = 15
nn = n  # 초기화
answer = 1
for mylist in myList:
    remain = nn - len(mylist)
    if remain < 0:  # 넘침
        answer += 1
        nn = n
        nn -= len(mylist)
    elif remain > 0:  # 안넘침
        nn -= len(mylist)
    else:  # 딱 맞음
        if mylist == myList[len(myList) - 1]:  # 마지막이면
            continue
        else:
            nn = n
            answer += 1

print(answer)
print(myList)
