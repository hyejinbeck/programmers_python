# 모음 = [a,e,i,o,u] 이렇게 5가지 
# my_string 에서 모음만 제거 
# 그러고 제거한 값들만 answer 
# "the bus" -> "the bus" - 모음 -> "th bs"
# 모음이 아닌 것들만 나오게 


def solution(my_string):    #in bus
    words = "aeiou"     # 소문자
    answer = ''      # my_string 에서 소문자가 아닌 것들만 이루어져있음 
    
    for m in my_string:    # i , n , b , u , s 
        if m not in words:   # 위에 있는게 아닌 값들은 
            answer += m       # 모아라 
    
    return answer