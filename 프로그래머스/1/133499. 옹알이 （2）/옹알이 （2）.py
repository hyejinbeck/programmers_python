def solution(babbling):
    count = 0    # 조카가 발음할수있는 단어의 갯수 
    for b in babbling:
        # 해당 단어가 문자열에 포함되어있는 경우 (조카가 발음못해서 카운팅x)
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue    
        # 해당 단어가 연속해서 나오지 않는 경우 (조카가 발음할수있는경우)
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count

# def solution(babbling):
#     count = 0
#     for b in babbling:
#         if all(b[i] != b[i+1] for i in range(len(b) - 1)):
#             count += 1
#     return count