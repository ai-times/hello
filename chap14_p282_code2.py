while True : 
    query = input( "\n질문 입력 >> ") 
    if query.count("안녕") >= 1 : 
        print("안녕하세요. 만나서 반가워요.") 
    elif query.count("파이썬") >= 1 : 
        print("파이썬 재밌지요. 열심히 공부하세요.") 
    elif query.count("날씨") >= 1 : 
        print("비가 올 가능성이 있습니다.") 
    else : 
        print("질문을 이해하지 못했습니다.")
