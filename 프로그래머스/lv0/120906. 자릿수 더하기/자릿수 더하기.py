# def solution(n):   # string으로 "5672" 등 무작위의 숫자조합 
#     answer = 0     # 위의 숫자하나하나 더한 값 
#     num_list = list(map(str,n)) # 하나씩 문자로 분리 "5","6","7","2"
#     for i in num_list:  # 하나씩 불러온다. "5"->"6"->"7"->"2"
#         int(i)  # 숫자화로 변경 5 + 6 + 7 + 2
#     return answer
# 일단 다시 해보자 
# n이 931 일때, answer값이 9+3+1인, 13이여야 한다. 
# 931 -> 9 , 3  , 1 -> 각각 더하기 + ---> 더한 값 answer 
# 931 ->"9","3","1"-> answer 변수에 9 넣고 3 넣고 1 넣자.  

def solution(n):      # 931  
    answer = 0 
    strtype = str(n)  # "931"
    for s in strtype:  # "9", "3", "1"
        # inst(s) 는 각각 9, 3, 1 이 된다. 
        answer = answer + int(s)
    return answer

    