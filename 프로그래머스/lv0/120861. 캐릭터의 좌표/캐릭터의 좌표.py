def solution(keyinput, board):  
    # keyinput 입력한 방향키의 배열 
    # board 맵의 크기 
    # 좌표 이동 = column 과 row  [0][0]
    col = board[0]
    row = board[1]
    result = [0, 0]
    
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    return result