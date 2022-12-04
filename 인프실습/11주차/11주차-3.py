import random

a = []
def file_write(): #파일에 난수 30개를 쓰는 함수
    f_out = open('random10.txt', 'w') #random10.txt 파일을 쓰기모드로 불러옴
    for line in range(30): #1부터 10까지의 수를 30개 생성
        num = random.randrange(1, 11)
        f_out.write(f'{str(num)} ')
        a.append(str(num))

    print("\n파일 내용 : ", end="")
    for i in a:
        print(i, end=" ")
    print("\n")

def file_read(): #난수 각각의 개수와 가장 많이 생성된 난수 출력
    f_in = open('random10.txt', 'r') #random10.txt 파일을 쓰기모드로 불러옴
    count = [0 for i in range(11)]
    numbers = map(int, f_in.readline().split())
    sen_list = []
    for i in numbers:
        count[i] += 1
    for i in range(1, 11): #sen_list에 난수 개수와 가장 많이 생성된 난수를 출력한 것을 저장
        sen_list.append(f'{i}: {count[i]}개')
        print(f'{i}: {count[i]}개')
    sen_list.append(f'\'{count.index(max(count))}\' 숫자가 {max(count)}개로 가장 많이 나왔습니다 !')
    print(f'\'{count.index(max(count))}\' 숫자가 {max(count)}개로 가장 많이 나왔습니다 !')
    return sen_list #출력 내용을 리스트 형태로 반환

def file_alter(sen_list): #file_read 함수에서 출력한 내용을 random10.txt 파일에 추가해 수정함
    f_out = open('random10.txt', 'r+')
    for i in a:
        f_out.write(f'{i} ')
    f_out.write("\n===========================\n\n")
    for datas in sen_list:
        f_out.writelines(f'{datas}\n')
    f_out.write("\n===========================\n")
    print("파일 수정이 완료되었습니다!!!")

print("1 : 랜덤 파일 생성")
print("2 : 난수 카운트")
print("3 : 파일 수정")
print("4 : 종료")

while True: #조건문을 통해 어떤 함수를 불러올지 정하고 4를 입력하면 프로그램을 종료한다.
    n = int(input("입력 : "))

    if n == 1:
        file_write()
    elif n == 2:
        b = file_read()
    elif n == 3:
        file_alter(b)
    elif n == 4:
        print('프로그램을 종료합니다.')
        break




