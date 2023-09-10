def solution(my_string, s, e): # 슬라이싱 [시작값:종료값]
    answer = ''                 # my_string[s:e+1] 만 따로 추출하면 21Sremme
    words = my_string[s:e+1][::-1]  # 이걸 역순으로 [::-1] emmerS12
    answer = my_string[:s] + words + my_string[e+1:]
    return answer 