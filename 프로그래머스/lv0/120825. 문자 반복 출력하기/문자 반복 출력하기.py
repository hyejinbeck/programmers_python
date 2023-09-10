def solution(my_string, n):
    answer = ''
    for m in my_string : 
        # answer = m*n만큼  이렇게 단어 하나하나하나두개두개두개 
        answer += m*n
    return answer
