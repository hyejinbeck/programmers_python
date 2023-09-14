def solution(strArr):
    result = []
    for i in range(len(strArr)):
        if i % 2 == 0:             # 짝수번째 인덱스인 경우
            result.append(strArr[i].lower())  # 모든 문자를 소문자로 변환
        else:
            result.append(strArr[i].upper())  # 모든 문자를 대문자로 변환
    return result