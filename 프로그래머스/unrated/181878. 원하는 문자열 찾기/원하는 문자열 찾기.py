def solution(myString, pat):
    # myString이 "AbCdEfG" 일때, 
    # pat 이 "aBc" 이면 
    # 소문자,대문자 상관없이 안에 들어있으니, 1 
    
    if pat.lower() in myString.lower():  
        return 1 
    else:
        return 0  