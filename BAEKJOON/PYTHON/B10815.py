# 숫자 카드
import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
finds = list(map(int, input().split()))

cards_dict = {}
for card in cards:
    cards_dict[card] = 0

for find in finds: # O(n)
    if find in cards_dict: # dict에서 조회 O(1)
        print("1", end=" ")
    else:
        print("0", end=" ")



# for find in finds: # O(n*m)
#     if find in cards:
#         print("1", end=" ")
#     else:
#         print("0", end=" ")

