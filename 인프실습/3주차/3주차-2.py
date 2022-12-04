num1 = int(input("num1을 입력하세요: ")) #num1을 int형으로 변환해서 입력받음
num2 = int(input("num2을 입력하세요: ")) #num2를 int형으로 변환해서 입력받음
print("num1+num2 =",num1+num2," , type =",type(num1+num2))
print("num1-num2 =",num1-num2," , type =",type(num1-num2))
print("num1*num2 =",num1*num2," , type =",type(num1*num2))
print("num1/num2 =",round(num1/num2,3)," , type =",type(num1/num2)) #round함수를 이용해 소수점 아래 세번째 자리까지만 연산
print("num1%num2 =",num1%num2," , type =",type(num1%num2))
print("num1**num2 =",num1**num2," , type =",type(num1**num2))
print("num1//num2 =",num1//num2," , type =",type(num1//num2))