def solution(nums):
    answer = 0

    length = len(nums)
    nums.sort()
    result = []

    for num in nums:
        if num not in result and len(result) < length / 2:
            result.append(num)

    # print(result)
    answer = len(result)
    return answer