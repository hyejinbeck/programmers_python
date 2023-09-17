def solution(arr, k):    
    unique_numbers = set()  # 고유한 숫자를 저장
    result = []             # 결과 
    
    for num in arr:
        if num not in unique_numbers:
            unique_numbers.add(num)  # 새로운 숫자를 집합에 추가
            result.append(num)  # 결과 배열에 숫자를 추가합니다.

        # 만약 고유한 숫자의 개수가 k와 같아지면 결과를 반환하고 함수 종료합니다.
        if len(unique_numbers) == k:
            return result
    
    # k개보다 적은 수가 선택되면 나머지를 -1로 채웁니다.
    while len(result) < k:
        result.append(-1)
    
    return result