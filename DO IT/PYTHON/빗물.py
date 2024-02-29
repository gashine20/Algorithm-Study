H, W = map(int, input().split())

height = list(map(int, input().split()))

water = 0

# 왼쪽에서 높은거, 오른쪽에서 높은거를 찾아 양쪽에서 낮은쪽을 찾음
for i in range(1, W-1):
    left_max = max(height[:i])
    right_max = max(height[i+1:])

    compare = min(left_max, right_max)

    if height[i] < compare:
        water += compare - height[i]

print(water)