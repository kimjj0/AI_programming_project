import random
import matplotlib.pyplot as plt

num = random.randint(1,10) #1부터 10 중 난수 저장
n = [num * i for i in range(1, 11)]
y1 = [(n_ * 1000)**0.5 for n_ in n] #첫번째 함수
y2 = [(n_)**2 for n_ in n] #두번째 함수
for i in range(10):
    if y1[i] == y2[i]: #교점일때  same point 나타내기
        plt.text(n[i], y1[i], 'Same point')

plt.xlabel(f'{num}*n')
plt.ylabel(f'2plot about {num}')
plt.plot(n, y1, 'r--D') #빨간 점선으로 나타냄
plt.plot(n, y2, 'b*') #파란 별로 나타냄
plt.legend([f'root({num}*n*1000)', f'({num}*n**2)'])
plt.show()
