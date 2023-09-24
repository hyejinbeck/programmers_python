def solution(id_pw, db):    
    # 아이디와 비밀번호가 담긴 2차원 배열 id_pw
    # id_pw 와 db 는 [id, pw]
    # id_pw[0] == id , id_pw[1] == pw 
    if id_pw in db :    # 아이디와 비밀번호가 모두 있다면
        return 'login'  # "login"을 return
    
    else :              # 실패 했을 때, 
        for id in db :  # 아이디 일치 
            if id[0] == id_pw[0] :   
                return 'wrong pw' 
        else :              # 아이디 미일치 
            return 'fail'