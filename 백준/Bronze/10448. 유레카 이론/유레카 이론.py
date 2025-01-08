import sys

input = sys.stdin.readline

T = [n * (n + 1) // 2 for n in range(1, 46)]

testcase = int(input())
K = [int(input()) for _ in range(testcase)]


def is_eureka(num):
    for t1 in T:
        if t1 > num:
            break
        for t2 in T:
            if t1 + t2 > num:
                break
            for t3 in T:
                total = t1 + t2 + t3
                if total == num:
                    return 1
                if total > num:
                    break
    return 0


for k in K:
    print(is_eureka(k))
