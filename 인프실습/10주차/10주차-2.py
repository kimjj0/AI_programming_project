class Animal: #Animal 클래스 생성
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Animal='+'\''+self.name+'\''

list_ani = [] #객체를 담을 리스트 생성
list_order = ['st','nd','rd']

for i in range(1, 4):
    ani = Animal(input(f'{i}{list_order[i-1]} Ani: ')) #3개의 객체를 생성
    list_ani.append(ani) #list_ani 리스트에 객체 삽입

for i in range(3): #__str__을 통해 출력
    print(list_ani[i])


