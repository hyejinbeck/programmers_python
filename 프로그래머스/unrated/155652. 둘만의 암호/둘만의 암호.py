def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳으로 시작 
    
    for sk in skip: # sh => skip의 문자 하나하나 꺼내서 
        if sk in alpha:    # skip문자는 알파벳에서 제외 
            alpha = alpha.replace(sk, "")  
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)] # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer
    