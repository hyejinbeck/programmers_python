def solution(board, moves):
    dollpop = 0   # 터트려진 인형 갯수  
    bucket = []  # 바구니 
    
    for move in moves:    # 인형뽑기 게임 하나하나 
        for row in board:     # board 판에 있는 row 에서 
            # row 그 줄의 [move-1] 맨 위에 있는 인형 
            if row[move-1] != 0:       # 게임하나에서 인형이 있으면 
                bucket.append(row[move-1])   # bucket에 더한다. 
                row[move-1] = 0         # row줄에 인형이 없으면 
                break                   # 멈춤 

        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            # bucket에 2개이상 이고, 맨위인형과 2번째인형이 같으면 
            dollpop += 2     # 인형2개 터진거 추가 
            bucket = bucket[:-2] # 그리고 그 2개 제거 
            
    return dollpop