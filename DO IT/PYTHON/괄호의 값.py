letter = list(map(str, input()))

print(letter)

bracket = '()'
sqBracket = '[]'

word = letter.pop()
sum = 0
bundle = 1

while letter:
    next = letter.pop()
    if bracket in next + word:
        print(next + word)
        word = word[1:len(word)]
        bundle *= 2
        print("bundle =", bundle, "sum =", sum)

    elif sqBracket in next + word:
        print(next + word)
        word = word[1:len(word)]
        bundle *= 3
        print("bundle =", bundle, "sum =", sum)

    else:
        word = next + word

    if word == '':
        sum += bundle
        bundle = 1

    # print(next)
