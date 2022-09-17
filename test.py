name = input('이름을 입력하세요. ')
height = int(input('키(cm)를 입력하세요. '))
weight = int(input('몸무게(kg)를 입력하세요. '))
BMI = round(weight/(height**2), 2)

print(f'{name}님의 키는 {height} cm이고 몸무게는 {weight} kg입니다.\nBmi 지수는 {BMI} 입니다')