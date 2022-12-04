import random
lotto_answer = [2, 5, 22, 32, 34, 39, 45] #1036회차 로또 당첨번호
lotto_set = set() #랜덤으로 받을 로또번호를 set 자료형으로 초기화
temp = []
lotto_number = random.randint(1, 45)
print(f'1036회차 당첨번호: {lotto_answer}\n')
for i in range(5): #로또번호 5줄를 받는 반복문
    for k in range(7): #1줄 당 7개의 숫자를 받는 반복문
        while lotto_number in lotto_set:
            lotto_number = random.randint(1, 45) #랜덤으로 숫자 받음
        lotto_set.add(lotto_number)

    j = 8 - len(lotto_set.intersection(lotto_answer)) #등수를 출력하기 위한 변수

    temp.append(j) #temp 리스트에 j를 넣느다
    lotto_list = list(lotto_set) #로또 번호를 set에서 list로 변경
    lotto_list.sort() #오름차순 정렬
    print(f'Lotto Number{i + 1} : {lotto_list}')
    lotto_set.clear()
print()
if j >= 6: #2개가 같아도 꽝
    print("꽝입니다!")
else:
    print(f'{min(temp)}등 당첨입니다!') #temp 리스트에서 가장 작은 temp값 출력





