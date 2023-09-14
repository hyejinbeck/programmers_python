def solution(arr):
    stk = []  
    i = 0  

    while i < len(arr):
        if not stk:          # stk에 아무것도 없을경우, 
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:  
            stk.pop()           # 마지막 값 제거
            i += 1
        else:               # stk 마지막 원소와 arr[i]가 다른 경우
            stk.append(arr[i])
            i += 1

    if not stk:        
        return [-1]
    else:
        return stk
