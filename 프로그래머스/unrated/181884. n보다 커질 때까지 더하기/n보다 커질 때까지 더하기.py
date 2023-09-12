def solution(numbers, n): # [58, 44, 27, 10, 100] 이고 139일때 
    answer = 0             # 조건에 맞을때, 원소들의 합을 담을거임 
    test = 0                
    
    for num in numbers:    # 일단 리스트 안에 하나씩 꺼내기 
        test += num       # 일단 test에 하나씩 더해 
                                # 만약에 
        if test > n:       # 다 더해진 값이 n보다 커지면, 
            return test 
    
    return test
