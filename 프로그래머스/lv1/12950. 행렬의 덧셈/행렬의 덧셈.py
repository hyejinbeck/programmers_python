def solution(arr1, arr2):
    answer = []
    
    # arr1 = [[1,2],[2,3]]
    # arr2 = [[3,4],[5,6]] 
    # answer = [[4,6],[7,9]]
    
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])
            
    return answer