def solution(number, limit, power):
    num = []
     
    for i in range(1,number+1):
        cnt = 0
        
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                cnt+=1
                if j < i//j:
                    cnt+=1
        num.append(cnt)
        
    for z in range(len(num)):
        if num[z] > limit:
            num[z] = power
    
    return sum(num)