# n = 10 = a * b 일때, a와b는 각각 1,2,5,10 
# n = 15 = a * b 일때, a와b는 각각 1,3,5,10 
# n = 33 = a * b 일때, a와b는 각각 1,3,11,33 
# 범위)  a와b는 1부터 n 까지의 범위를 가지고 있다. (슬라이싱 사용시 n+1 종료값)
# 조건)  n 나누기 a 했을때 나머지값이 0으로 떨어져야함 
# a의 갯수 = answer += 

def solution(n):       # n = 20 
    answer = 0             # a의 갯수를 담을 변수
    
    for a in range(1,n+1):     # 범위 (1부터 n포함해서)
        if n % a == 0 :         # 조건 (나눴을때 나머지값 0)
            answer +=1          # 카운팅 
    
    return answer