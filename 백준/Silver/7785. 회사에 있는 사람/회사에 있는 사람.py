# 회사에 있는 사람

check_list = {}
n = int(input())

for _ in range(n):
    name, state = input().split()

    if state == "enter":
        check_list[name] = state
    elif state == "leave":
        check_list.pop(name)

d = sorted(check_list, reverse=True) # O(n logn)

for cl in d:
    print(cl)