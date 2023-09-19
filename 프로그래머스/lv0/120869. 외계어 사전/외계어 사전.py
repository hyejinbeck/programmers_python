def solution(spell, dic):
    def can_construct_word(word):
        # word 안에 있는 각 문자의 개수를 세는 딕셔너리를 생성함
        word_count = {}
        for char in word:
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1
        
        # spell에 있는 알파벳을 사용하여 word를 만들 수 있는지 확인합니다.
        for char in spell:
            if char in word_count and word_count[char] > 0:
                word_count[char] -= 1
            else:
                return False
        
        return True

    for word in dic:
        if can_construct_word(word):
            return 1

    return 2