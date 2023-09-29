def solution(strings, n):
    answer = []

    chars = []

    strings.sort()
    for string in strings:
        chars.append(string[n])

    # print(chars)
    chars.sort()

    for i in range(len(strings)):
        for string in strings:
            if chars[i] == string[n]:
                if string not in answer:
                    answer.append(string)
                    break
    return answer