import random
import matplotlib.pyplot as plt
import time

start = time.time() #시작 시간 저장
num = []
num_count = []
for i in range(30):
    num.append(random.randint(1, 10)) #1부터 10까지의 난수 30개 num 리스트에 저장

for i in range(1, 11):
    num_count.append(num.count(i)) #각 숫자의 개수 리스트에 저장

plt.pie(num_count) #그래프 생성
plt.title("Random Num Graph")
plt.legend(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
plt.show()
end = time.time() #끝난 시간 저장
print("-------------------------------")
print("[프로그램 실행일자]")
print(time.asctime())  #실행일자 출력
print("-------------------------------")
print(f'프로그램 시작시간: {start}')
print(f'프로그램 마감시간: {end}')
print("-------------------------------")
print(f'프로그램 수행시간: {end - start}') #프로그램 수행시간 출력
print("-------------------------------")
print(f'생성된 난수 30개: {num}')
print(f'숫자별 난수 빈도수: {num_count}')
print("-------------------------------")


