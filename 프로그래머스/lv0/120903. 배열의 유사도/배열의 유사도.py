def solution(s1, s2): # s1, s2 에는 각각 어떤수가 올지 모름 
    answer = 0     # s1, s2 가 공통 원소를 갖는 갯수를 담을꺼 
    for a in s1 :   # 일단 하나하나 s1 숫자 꺼내서 
        if a in s2 :  # 그 값이 s2 에도 있다면, 
            answer += 1 # 하나씩 카운팅 
    return answer