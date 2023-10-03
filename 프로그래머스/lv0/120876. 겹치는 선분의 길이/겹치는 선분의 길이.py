def solution(lines):
    # a,b의 범위는 -100부터100까지니까 전체범위는 200이다. 
    # 중복없이, 순서없이 set 이용 
    table = [set([]) for _ in range(200)]
    
    # 2차원 배열 lines가 매개변수니까 index, line 으로 따로 
    for index, line in enumerate(lines):
        # line을 또 x1, x2로 변수화 
        x1, x2 = line
        
        for x in range(x1, x2):
            table[x + 100].add(index)   

    answer = 0
    
    for line in table:       # 하나씩 line을 꺼내서 
        if len(line) > 1:     # 1을넘으면 겹치는 부분 
            answer += 1         # 하나씩 카운팅 

    return answer