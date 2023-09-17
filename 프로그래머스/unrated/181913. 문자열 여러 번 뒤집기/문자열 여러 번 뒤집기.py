def solution(my_string, queries):
    # reverse 는 리스트를 뒤집는 용도이며, 문자열에서는 X 
    # 슬라이싱 [:] 으로 바꾸기 
    # s 인덱스부터 
    # e 인덱스까지 
    # queries sms [s:e] 가 몇 가지있어서 실행 해야한다. 
    
    for s, e in queries:      # "rermgorpsam"
      # [2,3]                 # "remrgorpsam" 
                              # ~1번 인덱스 고정  [:s]는그대로
                              # 2,3인덱스만 바뀜  [s:e+1]를역순
                              # 4번~ 인덱스 고정  [e+1:]는그대로
      # [0,7] 
      # [5,9] .... 
      
      my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    
    return my_string
