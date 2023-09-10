# my_string 안에 값 하나하나 꺼내서 
# int 값인지 확인  = 숫자값인지 확인하는 함수는 .isdigit() 
# 참고로 문자열인지 확인하는건 isalpha() 
# int 값들이라면, 모아서 각각 더하기 sum() 

def solution(my_string):  # 1a2b3c 라면 
    answer = 0
    
    for m in my_string:  # 1, a, 2, b, 3 ,c 하나하나 
        if m.isdigit():     # 숫자값인지 확인 
            #answer += m   # error 'int'가 될수도 'str'될수도? 
            answer += int(m)
    
    return answer