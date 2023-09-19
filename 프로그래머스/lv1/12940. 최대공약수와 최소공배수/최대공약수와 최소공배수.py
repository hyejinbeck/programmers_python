def solution(n, m):
    answer = []
    # 최대 공약수 구하기
    for i in range(1,m if m >= n else n) :
        if n % i == 0 and m % i == 0 :
            max = i
    answer.append(max)
    # 최소 공배수 구하기
    min = (m * n) // max
    answer.append(min)
    return answer
