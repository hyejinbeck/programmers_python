def solution(str_list):                 # ["l"]
    
    for i in range(len(str_list)):     # 일단 안의 값들 다 돌려보자. 
        if str_list[i] == "l":          # 그중 l 이면 
            return str_list[:i]          # l이 오른쪽에 있어야하고 
        elif str_list[i] == "r":       # r이면 
            return str_list[i+1:]      # r의 왼쪽부터 저장해라 
    
    return []