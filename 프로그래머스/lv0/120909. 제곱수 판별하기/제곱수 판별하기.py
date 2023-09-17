def solution(n):
    answer = 0
    # 제곱근 ? 
    # 9 의 제곱근 = 3 .... 
    # 3 **2 == 9 
    # 9 **0.5 == 3 
    answer = int(n ** 0.5) 
    
    if answer * answer == n: 
        return 1 
    

    return 2 
