depth = int(input("별찍기 깊이 입력 : ")) #별찍기 깊이 입력

for i in range(depth): #깊이만큼 반복
    if i < (depth // 2): #큰 삼각형을 반으로 나누었을 때 윗부분
        for x in range(depth - i):
            print(" ", end="") #윗부분 왼쪽 공백 출력
        for x in range(2 * i + 1):
            print("*", end="")
    else: #큰 삼각형을 반으로 나누었을 때 아랫부분
        for x in range(depth - i):
            print(" ", end="") #아랫부분 왼쪽 공백 출력
        for x in range(2 * i + 1 - depth):
            print("*", end="")
        for x in range(depth - (2 * i+ 1 - depth)):
            print(" ", end="") #큰 삼각형 중앙의 공백 출력
        for x in range(2 * i + 1 - depth):
            print("*", end="")
    print()

