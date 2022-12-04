import math
from random import randint as r
from math import sqrt as s
from math import pow as p

print(dir(math)) #라이브러리의 내장함수를 나타내는 함수 dir 사용
print("\n\n")

count = 0 #입력 횟수를 위한 변수
x1 = r(1, 10) #4개의 변수에 각각 1부터 10까지의 랜덤 수 저장
x2 = r(1, 10)
y1 = r(1, 10)
y2 = r(1, 10)
ans = s((p((x2 - x1),2) + p((y2 - y1), 2))) # 두 점 사이의 거리를 구한 값을 ans에 저장
print("두 점 사이의 거리는 :", ans)
while True: #하나씩 맞았을 때와 둘 다 틀렸을 때, 둘 다 맞았을 때 4개로 조건을 나눠 반복
    ans_list = input('(x2-x1)의 값과 (y2-y2)의 값을 맞추시오. ').split() #입력값을 띄어쓰기로 구분해 저장
    my_ans1, my_ans2 = map(int, ans_list) #저장한 값을 정수형으로 변환
    if my_ans1 == abs(x2 - x1) and my_ans2 != abs(y2 - y1):
        count += 1 #입력횟수 1 증가
        print("x2-x1의 값만 정답입니다..")
    elif my_ans1 != abs(x2 - x1) and my_ans2 == abs(y2 - y1):
        count += 1
        print("y2-y1의 값만 정답입니다..")
    elif my_ans1 != abs(x2 - x1) and my_ans2 != abs(y2 - y1):
        count += 1
        print("둘 다 틀렸습니다..!")
    else:
        count += 1
        print(f'{count} 만에 정답입니다!')
        break

