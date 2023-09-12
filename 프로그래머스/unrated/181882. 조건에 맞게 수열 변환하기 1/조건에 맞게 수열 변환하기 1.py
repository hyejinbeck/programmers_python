def solution(arr):       # [1,2,3,100,99,98] 일때, 
    result = []

    for num in arr:         # 일단 하나씩 꺼내 
        if num >= 50 and num % 2 == 0:  # 50보다 크거나같은 & 짝수라면
            result.append(num // 2)         # 2로 나눈 값을 추가 
        elif num < 50 and num % 2 == 1:  # 50보다 작 & 홀수라면 
            result.append(num * 2)          # 2를 곱한 값을 추가 
        else:                            
            result.append(num)   # 바꾸지 않고 저장 
    
    return result