중간 = int( input("중간고사 점수 입력 : ") ) 
기말 = int( input("기말고사 점수 입력 : ") ) 
평균 = (중간+기말) / 2 
if 평균 >= 80 :
    print("본 과목을 성공적으로 통과하셨습니다. ")
else : 
    print("아쉽게도 시험에서 탈락하셨습니다. ")
    print("다음 기회에 도전해주세요.")
print("즐거운 방학 보내세요.")

print("당신의 평균점수는 %.2f점 입니다." % 평균)
print("당신의 평균점수는 {0:.2f}점 입니다.".format(평균) )     # format 함수 활용
