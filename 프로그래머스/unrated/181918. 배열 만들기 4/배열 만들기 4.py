# arr 이 [1,4,2,5,3] 일때, 
# 정답인 stk 값은 [1,2,3] 이다. 
# arr --> 변형 ---> stk 

def solution(arr):    # [1,4,2,5,3]
    stk = []             #  정답 넣을 빈 리스트 
    i = 0                   # 인덱스 변수 초기화

    while i < len(arr):    
        if not stk:         # stk 비어있을때 
            stk.append(arr[i])   # stk에 i를 더하고 
            i += 1             # i에 1을 더해라 
        elif stk[-1] < arr[i]:   # stk마지막원소가 arr[i]작다면 
            stk.append(arr[i])   # stk에 arr[i]를 더하고 
                        # 어자피 뒤에 추가됨 
            i += 1              # i 에 1을 더해라 
        else:
            stk.pop()       # 어자피 마지막을 제거해줌 

    return stk
                
    
    
    
    