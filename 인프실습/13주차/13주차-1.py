import random
import matplotlib.pyplot as plt

all_num = []
count_neg = 0 #음수 개수 0으로 초기화
count_pos = 0 #양수 개수 0으로 초기화
for i in range(11):
    num = random.randint(-10, 10) #-10부터 10 까지 난수 저장
    all_num.append(num) #열번 반복하며 all_num에 저장
    if num < 0:
        count_neg += 1 #음수 개수 증가
    elif num >= 0:
        count_pos += 1 #양수 개수 증가

x = range(1, len(all_num)+1)
plt.title("(-10 ~ 10) bar")
if count_neg > count_pos: #음수가 더 많을 때 그리기
    plt.bar(x, all_num, width=0.5, color="blue")
else: #양수가 더 많을 때 그리기
    plt.bar(x, all_num, width=0.5, color="red")

plt.show()


