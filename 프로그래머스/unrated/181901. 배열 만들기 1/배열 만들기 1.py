def solution(n, k):     # n이 10이고, k가 3일때 
    answer = []       # 정답값 담을 변수 
                     # 정답은 [3,6,9] 가 되어야함 
                    # k부터, k*2, k*3 ... n까지 (n포함)
    
    for i in range(k, n+1, k):
        answer.append(i)
    
    return answer