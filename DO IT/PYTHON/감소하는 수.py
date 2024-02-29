n = int(input())

reduce = []

nums = []
for i in range(10):
    nums.append(str(i))

cnt = 1
while cnt < 10:
    for i in nums:
        if len(i) == cnt:
            for j in range(10):
                if int(i[-1]) > j:
                    nums.append(i + str(j))

    cnt += 1

num = 0

# print(reduce)
if n > 1022:
    print(-1)
else:
    print(nums[n])
