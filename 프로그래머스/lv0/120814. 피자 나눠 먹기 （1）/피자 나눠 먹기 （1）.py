def solution(n):      # 1판에 7조각은 고정값 
    answer = 0
    if n <= 7:        # 일단 7명 이하는 무조건 1판 
        answer = 1
    else:               # 7명이 넘어가면 
        if n % 7 == 0:        # 14명 나누기 7조각은 2판 
            answer = n // 7
        else:           # 깔끔하게 안떨어질땐 
            answer = (n // 7) + 1   # 1판 더 시키면 된다. 
    return answer