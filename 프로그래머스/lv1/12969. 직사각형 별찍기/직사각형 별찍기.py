n, m = map(int, input().strip().split(' '))
# 5 3 ---> "5""3"

# 세로의 길이 m만큼 반복한다. 
for _ in range(m):
    # 가로의 길이 n만큼 별(*)을 출력한다. 
    print('*' * n)