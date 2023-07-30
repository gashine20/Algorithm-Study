def solution(s, skip, index):
    answer = ''

    for i in s:  # "aukks"
        next = ord(i)
        count = 1
        idx = 0

        while (count <= index):
            # print(idx)
            idx += 1
            if chr(next + idx) in skip:  # skip에 포함되어 있으면
                pass
            else:  # 포함 안되어 있으면
                if next + idx >= 122:  # z 넘고
                    idx -= 26
                count += 1

        next = next + idx
        answer += chr(next)

    return answer