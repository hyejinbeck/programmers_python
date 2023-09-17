def solution(arr, k):
    # arr 배열 중에 뭔갈 찾아야 한다. 
    # k는 그 중에 무작위로 주워진뒤,,,
        # 지금까지 나온적없는 수의 갯수만큼 배열 뒤에 추가 
        # 어떻게 한다음에 결국 만들어진 길이 
    
    answer = []  # 결과
    counting = 0  # 지금까지 나온적이 없는 수의 갯수 카운팅 
    
    for num in arr:  # 일정한 범위 내에서 무작위로 수를 뽑은 후
        if num not in answer:  #  지금까지 나온적이 없는 수이면
            answer.append(num)  # 배열 맨 뒤에 추가
            counting += 1  # 그리곤 몇개인지 카운팅 
            # 이건 결국, 중복되지 않는 수의 갯수 
        
        if counting == k:  # 그 갯수가 결국 만들어질 길이 k 라면 종료
            break
    
    # 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return
    while len(answer) < k:
        answer.append(-1)
    
    return answer