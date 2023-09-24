def solution(board, moves):
    # board = 인형들 들어있는 2차원 배열 (col, row) 
    # 0 부터 시작함 
    # moves = 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열
    # bascket =  집어 올린 인형은 바구니에 쌓임 (순서대로 5개)
    # answer = 터트려져 사라진 인형의 개수 
    basket = []
    answer = 0

    for move in moves:
        # board의 열인덱스는 0부터 시작
        # moves의 배열값은 1부터 시작함 -1 = 0 으로 맞춰줌 
        # move = -1 불가 (열의 위치 제대로 매치 안됨))
        move -= 1      #(-1부터 시작하게 )
        
        # board 에서 인형을 하나씩 꺼냄 
        for i in range(len(board)):
            if board[i][move] != 0:
                doll = board[i][move]
                board[i][move] = 0  # 인형이 집혔으므로 해당 칸을 0으로 만듭니다.
                
                if basket and basket[-1] == doll:
                    # 바구니의 맨 위 인형과 현재 집은 인형이 같으면 터트립니다.
                    basket.pop()
                    answer += 2  # 터진 인형 2개를 결과에 추가합니다.
                else:
                    basket.append(doll)
                break  # 크레인 동작을 마쳤으므로 다음 크레인으로 넘어갑니다.

    return answer