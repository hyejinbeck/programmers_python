# ice_a = 5500
# money = 머쓱이가 가지고 있는 돈 
# money가 5500일때, (money 나누기 ice_a) 해서 나눈 몫과 나머지의 값 
# 나눈 몫 = coffee = money // ice_a
# 나머지 = pockey_money = money % ice_a 
# answer = [coffee,pocket_money]


def solution(money):            # 5,500원일때 
    ice_a = int(5500)
    coffee = money // ice_a   # 나누기 커피가격의 몫 = 몇 잔 
    pocket_money = money % ice_a # 나머지 = 잔돈 
    
    return [coffee,pocket_money]