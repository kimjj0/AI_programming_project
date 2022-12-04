num = int(input("피보나치 숫자 입력: ")) #출력할 개수 num 변수에 입력
a = 1
b = 1
for i in range(num):
    print(a, end="  ")
    a, b = b, a + b #다중 대입을 통해 a에 b 값을 넣는 동시에 b에 a + b 값을 넣는다