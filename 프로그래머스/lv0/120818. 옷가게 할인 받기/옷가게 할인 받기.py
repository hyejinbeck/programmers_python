# price >= 100000 일때, result = price-(price의 5%)
# price >= 300000 일때, result = price-(price의10%)
# price >= 500000 일때, reuslt = price-(price의20%)


def solution(price):        
    if price >= 500000 : 
        answer = price * 0.8
    elif price >= 300000 : 
        answer = price * 0.9
    elif price >= 100000 : 
        answer = price * 0.95 
    else: 
        answer = price 
    return int(answer)