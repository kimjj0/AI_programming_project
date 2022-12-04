import random
lastlotto = [2, 5, 22, 32, 34, 39, 45]
lotto_set = set()
temp = []
print("1036회차 당첨번호:", lastlotto, "\n")
def lotto_gen():
    lotto_number = random.randint(1, 45)
    for k in range(7): #1줄 당 7개의 숫자를 받는 반복문
        while lotto_number in lotto_set:
            lotto_number = random.randint(1, 45) #랜덤으로 숫자 받음
        lotto_set.add(lotto_number)

def lotto_print():
    lotto_all = []
    for i in range(5): #lotto_gen() 5번 반복해 로또 5줄 얻음
        lotto_gen()
        lotto_list = list(lotto_set)
        lotto_list.sort()
        print(f'Lotto Number{i+1} : {lotto_list}')
        lotto_all.append(lotto_list)
        lotto_set.clear()
    return lotto_all

def lotto_check(lastlotto, lotto_all): #당첨된 로또가 있는지 확인하는 함수
    for i in range(5):
        lotto_set1 = set(lotto_all[i])
        j = 8 - len(lotto_set1.intersection(lastlotto)) #당첨번호와 얼마나 겹쳤는지 확인하는 변수
        temp.append(j)
    if min(temp) > 5: #6개 이상 다르면 꽝
        print("꽝입니다!")
    else:
        print(f'{min(temp)}등 당첨입니다!')

lotto_all = lotto_print()
print("\n")
lotto_check(lastlotto, lotto_all)






