import random

for t in range (5) : 
    a = random.randint(2,9)
    b = random.randint(2,9)
    dab = a * b 
    print( )
    n = int( input( "[문제%d]  %d x %d = " % (t+1,a,b) ) )
    if n==dab :
        print("맞췄습니다.")
    else :
        print("땡! 틀렸습니다.")
