def solution(n, arr1, arr2):
    answer = []
    arr3 = []
    arr4 = []
    for i in range(n):
        arr3.append(bin(arr1[i])[2:])
        arr4.append(bin(arr2[i])[2:])
        arr3[i] = ('0' * (n-len(arr3[i]))) + arr3[i]
        arr4[i] = ('0' * (n-len(arr4[i]))) + arr4[i]
    
        tmp = ''
        for p in range(n):
            if arr3[i][p] == '1' or arr4[i][p] == '1':
                tmp += '#'
            elif arr3[i][p] == '0' and arr4[i][p] == '0':
                tmp += ' '
        answer.append(tmp)
        
    return answer