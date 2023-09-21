def solution(picture, k):   
    # picture 그림파일의 문자열 배열 
    # picture 그림파일을 k배로 가로세로 늘린 그림파일 = answer 저장 
    answer = []
    # row, column 
    
    for row in picture: # 일단 picture 
        resized = ''
        
        for pixel in row:
            resized += pixel * k # 한 픽셀을 k배 만큼 가로로 늘린다.
        
        for _ in range(k):
            answer.append(resized) # 가로로 늘려진 이미지 한 줄을 k배 만큼 세로로 늘린다. 
    
    return answer