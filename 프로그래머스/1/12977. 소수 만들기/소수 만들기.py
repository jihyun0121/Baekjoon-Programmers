def solution(nums):
    answer = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum_num = nums[i] + nums[j] + nums[k]

                for x in range(2, round(sum_num/2)):
                    if sum_num % x == 0:
                        break
                else:
                    answer += 1
    return answer