print("두 정수에 대한 최대공약수를 구합니다.")
n1 = int(input("작은 수 입력 : "))
n2 = int(input("큰 수 입력 : "))
gcd = 1
t = 2 
while t <= n1 :
    if (n1%t==0) and (n2%t==0) :
        gcd = t
    t += 1
print("%d와 %d의 최대공약수는 %d 입니다." % (n1, n2, gcd) ) 
