def solution(numbers, hand):
    # numbers = 순서대로 누를 번호가 담긴 배열 
    # hand = 왼손잡이인지 오른손잡이인지 나타내는 문자열 
    result = ""   # 연속된 문자열 형태로 return 
    l_pos = 10    # * 인데 10으로 숫자화  
    r_pos = 12    # # 인데 12으로 숫자화 

    for number in numbers: 
        # 0입력할땐 그냥 11로 해버림 
        if number == 0:
            number = 11

        if number in [1,4,7]:       # 1, 4, 7은 왼손으로 입력
            result += 'L'
            l_pos = number
        elif number in [3,6,9]:     # 3, 6, 9는 오른손으로 입력
            result += 'R'
            r_pos = number
        else:
             # 숫자가 2,5,8,11(0대체값)중하나일때,어떤손을 사용할지 결정
            big = max(number, l_pos)
            small = min(number, l_pos)
            l_gap = (big-small) // 3 + (big-small) % 3

            big = max(number, r_pos)
            small = min(number, r_pos)
            r_gap = (big-small) // 3 + (big-small) % 3
            
            if l_gap > r_gap:
                result += 'R'  # 오른손의 이동 거리가 더 가까우면 오른손으로 입력
                r_pos = number
            elif l_gap < r_gap: # 왼손의 이동 거리가 더 가까우면 왼손으로 입력
                result += 'L'
                l_pos = number
            else:
                if hand[0] == 'l': # 이동 거리가 같을 때, 왼손잡이이면 왼손
                    result += 'L'
                    l_pos = number
                else:
                    result += 'R'   # 이동 거리가 같을 때, 오른손잡이이면 오른손
                    r_pos = number

    return result