def solution(slice, n):  
    answer = 0 
    if n % slice == 0 :   # 14명 나누기 3조각 해서 깔끔하게 값이 떨어지면 
        answer = n // slice    # 총 4조각 필요 
    else:                 # 14명 나누기 5조각 해서 나머지값 생길때, 
        answer = (n // slice ) + 1 # 한 판 더 시키면 됨 
    return answer
