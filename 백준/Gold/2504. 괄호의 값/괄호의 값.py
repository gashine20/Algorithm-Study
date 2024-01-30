import sys

input = sys.stdin.readline

bracket = list(map(str, input()))

stack = []  # 스택
res = 1  # result에 더해주기 전 임시 변수
result = 0  # 결과 변수

# 열린 괄호만 스택에 넣고, 닫힌 괄호를 만나면 스택의 top을 꺼내 쌍을 맞춤
# 열린 괄호로 2,3 곱하기 계산

# 1~4번째 과정 시작
for i in range(len(bracket)):
    if bracket[i] == '(':
        res *= 2
        stack.append(bracket[i])

    elif bracket[i] == '[':
        res *= 3
        stack.append(bracket[i])

    elif bracket[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if bracket[i - 1] == '(':
            result += res
        res //= 2
        stack.pop()

    elif bracket[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if bracket[i - 1] == '[':
            result += res
        res //= 3
        stack.pop()

# 결과 출력
if stack:
    print(0)
else:
    print(result)
