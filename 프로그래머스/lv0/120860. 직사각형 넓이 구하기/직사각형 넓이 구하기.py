def solution(dots):
    # return 직사각형의 넓이
    # 직사각형의 넓이 = 가로 * 세로 
    # 가로좌표 = 
    # 세로좌표 = 
    weight = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]
    
    return weight*height