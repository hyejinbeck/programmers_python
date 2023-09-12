def solution(my_string):                # int + str - ins,,,         
    numbers = my_string.split()         # "int","+또는-","int" ... 
    # print(numbers) 하면 	['3', '+', '4'] 
    answer = int(numbers[0]) 
    # 처음 숫자로 시작한다! 
                                             #  0134 ....... 
    for n in range(1, len(numbers),2 ):      # "4+2-2"
                                                # 인덱스 1번부터 시작 4는 제외 
        if numbers[n] == "+":              
            answer = answer + int(numbers[n+1])      # 더해라 
        elif numbers[n] == "-":                      # 중간이 - 라면 
            answer = answer - int(numbers[n+1])       # 빼라  (그 다음 인덱스 요소)
    
    return answer