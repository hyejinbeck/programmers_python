def solution(arr1, arr2):
    # 두 배열의 길이를 비교하기위해, 일단 두 배열의 길이 각각 구해야함 
    len1 = len(arr1)
    len2 = len(arr2)
    
    #두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1
    
    # 배열의 길이가 같다면 
    # 각 배열에 있는 모든 원소의 합을 비교하여   --> arr1,arr2의 원소의 합
    # 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    
    if sum1 < sum2:
        return -1
    elif sum1 > sum2:
        return 1
    
    return 0
