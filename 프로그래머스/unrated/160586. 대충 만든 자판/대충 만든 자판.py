def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for i in target:
            idx = []
            for keys in keymap:
                if i in keys:
                    idx.append(keys.index(i) + 1)  # keymap에서 해당 문자의 위치 인덱스를 찾아 idx 리스트에 추가
            if idx:
                min_idx = min(idx)  # idx 리스트에서 가장 작은 값 찾기
                count += min_idx  # 가장 작은 값만큼 누르기
            else:
                count = -1  # 찾지 못한 경우
                break  # 현재 문자열은 더 이상 계산할 필요 없으므로 루프 종료
        answer.append(count)
    return answer