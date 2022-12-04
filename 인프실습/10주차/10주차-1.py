class Animal: #Animal 클래스 생성
    def __init__(self, name, color, legs):
        self.name = name
        self.color = color
        self.legs = legs

class Dog(Animal): #Animal 클래스 상속 받는 Dog 클래스 생성
    def show_info(self): #출력 함수 선언
        print(f'이름 : {self.name}, 색상 : {self.color}, 다리 수 : {self.legs}')

class Bird(Animal): #Animal 클래스 상속 받는 Bird 클래스 생성
    def show_info(self):
        print(f'이름 : {self.name}, 색상 : {self.color}, 다리 수 : {self.legs}')

class Whale(Animal): #Animal 클래스 상속 받는 Whale 클래스 생성
    def show_info(self):
        print(f'이름 : {self.name}, 색상 : {self.color}, 다리 수 : {self.legs}')

#각 상속 받은 클래스마다 객체 생성
ani1 = Dog("황구", "황색", "4")
ani2 = Bird("기러기", "하양", "2")
ani3 = Whale("흑등고래", "검정", "0")
#출력
ani1.show_info()
ani2.show_info()
ani3.show_info()




