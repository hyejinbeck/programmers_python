def solution(arr):       # 1,1,3,3,0,1,1, 
    # 함수를 완성하세요
    answer = []          # 1,3,0,1 (연속적으로 나타나는 숫자 1개만 제거)
    for a in arr:        # 일단 1,1,3,3,0,1,1 하나씩 꺼내서 
        if answer[-1:] == [a]: continue
        answer.append(a)
    return answer