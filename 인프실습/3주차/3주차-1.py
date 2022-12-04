num1 = input("num1: ")
num2 = input("num2: ")
num3 = int(num1) + float(num2) #num1을 정수형으로 num2를 실수형으로 형변환
print("num1 + num2 = ", num3, ",num3의 자료형: ", type(num3)) #type 함수로 num3의 자료형 확인
print("num2와 num3의 자료형이 같다?: ", type(float(num2)) == type(num3)) #연산자 ==로 같으면 두 개가 같으면 True 다르면 True
print("num2와 num3의 자료형이 다르다?: ", type(float(num2)) != type(num3)) #연산자 !=로 두 개가 같으면 False 다르면 True