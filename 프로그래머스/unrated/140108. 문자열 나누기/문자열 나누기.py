def solution(s):
    answer = 0
    # s = banana 일때, 
    # x = b 
    # b인 글자와, b가 아닌 글자들을 각각 카운팅 
    # 근데 왜 ba, na, na로 하는거지?
    word_x = 0 
    word_not = 0 
    for word in s :  # 일단 단어들을 하나하나 읽어가면서 분리 
        if word_x == word_not : 
            answer +=1  
            x = word
        if x == word: 
            word_x += 1 
        else: 
            word_not +=1 
    return answer