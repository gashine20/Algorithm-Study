def solution(s):
    answer = ''

    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    start = 0
    word = ''
    for i in range(len(s)):

        word = s[start:i + 1]

        if word.isdigit():  # 숫자이면
            answer += str(word)
            start = i + 1

        if word in words:
            answer += str(words.index(word))
            start = i + 1

    return int(answer)