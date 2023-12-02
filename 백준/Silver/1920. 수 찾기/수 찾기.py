# 이진트리
N = int(input())

numbers = list(map(int, input().split()))

M = int(input())
findNumbers = list(map(int, input().split()))

numbers.sort()


def secondary_tree(findNumber):
    start = 0
    end = len(numbers)-1
    middle = 0

    while start <= end:
        middle = int((start + end) / 2)
        if findNumber < numbers[middle]:
            end = middle - 1
        elif findNumber > numbers[middle]:
            start = middle + 1
        else:
            return 1
    return 0


for findNumber in findNumbers:
    print(secondary_tree(findNumber))
