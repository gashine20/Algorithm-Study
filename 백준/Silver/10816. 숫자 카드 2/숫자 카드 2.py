# 숫자 카드 2
import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
finds = list(map(int, input().split()))

# list -> dict
cards_dict = {}
for card in cards:
    if card in cards_dict:  # O(n)
        cards_dict[card] = cards_dict[card] + 1
    else:
        cards_dict[card] = 1

for find in finds:
    if find in cards_dict:
        print(cards_dict[find], end=" ")
    else:
        print(0, end=" ")
