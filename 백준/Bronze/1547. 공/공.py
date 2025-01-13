# 공
# 공은 position[1]에 있음

position = [i for i in range(0, 4)]


def switch(x, y):
    x_index = position.index(x)
    y_index = position.index(y)
    temp = position[x_index]
    position[x_index] = position[y_index]
    position[y_index] = temp


M = int(input())
for _ in range(M):
    X, Y = map(int, input().split())
    switch(X, Y)
    # print(position)

print(position[1])
