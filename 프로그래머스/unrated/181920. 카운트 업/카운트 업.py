def solution(start_num, end_num):
    # start_num 3 일때 
    # end_num 10이면, 
    # answer = start_num 부터 ~ end_num 까지 
    # range(start_num, end_num+1) 는 3부터 10까지 
    # 하나하나씩 차례대로 담기 
    answer = [] 
    for num in range(start_num, end_num+1): 
        answer.append(num)
    return answer
