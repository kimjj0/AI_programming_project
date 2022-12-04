from random import randint as r

ans = int(input("1 ~ 50 사이의 정답을 입력하세요! ")) #정답 입력
count = 0
computer_ans_arr = []
while True:
    computer_ans = r(1, 50) #1부터 50 중 랜덤한 수를 컴퓨터 정답으로 저장
    computer_ans_arr.append(computer_ans) #반복하며 컴퓨터의 정답을 list에 넣음
    count += 1
    if computer_ans == ans:
        if count <= 10: #컴퓨터의 정답이 맞고 입력횟수가 10 이하일 때 출력
            print("컴퓨터가 정답을 맞췄습니다!\n")
            print("[COMPUTER WIN!!]\n")
        else: #컴퓨터의 정답이 맞지만 입력횟수가 11 초과됐을 때 출력
            print("컴퓨터가 정답을 맞췄습니다!\n")
            print("[USER WIN!!]\n")
        break

for i, j in enumerate(computer_ans_arr): #enumerate를 이용해 순서와 그 값 출력
    print(f'Computer {i+1}번째 시도: {j}')


