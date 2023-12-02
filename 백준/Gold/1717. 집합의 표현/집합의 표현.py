# 유니온 파인드 알고리즘 (Union Find)
# 어떤 두 개의 노드를 같은 집합으로 묶어주고, 어떤 두 노드가 같은 집합에 있는지 확인하는 알고리즘
import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
arr = [i for i in range(n + 1)]


def find_index(number):
    if arr[number] != number:
        arr[number] = find_index(arr[number])
    return arr[number]


def arr_union(a, b):
    a_index = find_index(a)
    b_index = find_index(b)

    if a_index != b_index:
        arr[b_index] = a_index


def arr_find(a, b):
    a_index = find_index(a)
    b_index = find_index(b)

    if a_index == b_index:
        return "YES"
    else:
        return "NO"


for _ in range(m):
    question, a, b = map(int, input().split())
    if question == 0:
        arr_union(a, b)
        # print(arr)
    elif question == 1:
        print(arr_find(a, b))
