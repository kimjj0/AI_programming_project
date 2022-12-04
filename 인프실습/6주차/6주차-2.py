num = int(input('N값을 입력해주세요 : '))

for i in range(1, num+1): #1부터 num까지 반복
    is_Prime = True
    if i == 1:
        is_Prime = False #1은 소수에 포함하지 않음
    for j in range(2, i):
        if i % j == 0:
            is_Prime = False #i % j == 0 이면 소수가 아님
            break
    if is_Prime:
        print(i, end=" ") #소수면 띄어쓰기고 이어서 출력

