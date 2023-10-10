def solution(lottos, win_nums):
    cnt_corr = 0  # 맞춘 번호 개수 초기화 (최저 순위용)
    cnt_zero = 0  # 알아볼 수 없는 번호 개수 초기화
    for i in range(len(lottos)):
        if lottos[i] in win_nums:  # 로또 번호가 당첨 번호 중에 있다면
            cnt_corr += 1  # 맞춘 번호 개수를 증가시킴
        if lottos[i] == 0:  # 로또 번호가 0인 경우 (알아볼 수 없는 번호)
            cnt_zero += 1  # 알아볼 수 없는 번호 개수를 증가시킴
    total = cnt_corr + cnt_zero  # 당첨 가능한 최고 개수 계산
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}  # 순위와 당첨 내용에 대한 딕셔너리
    answer = [rank[total], rank[cnt_corr]]  # 최고 순위와 최저 순위를 리스트로 반환
    return answer