dict1 = {'Name': '김사랑', 'Age': 27, 'Hobby': ['독서', '음악감상'], 'Lang': ('Java', 'Python')}
dict1['gender'] = '여' #dict1에 'gender' key에 '여' value 추가
print(dict1)
print(dict1.get('Name'), type(dict1.get('Name'))) #'Name'의 value 값과 형태 출력
print(dict1.get('Age'), type(dict1.get('Age'))) #'Age'의 value 값과 형태 출력
print(dict1.get('Hobby'), type(dict1.get('Hobby'))) #'Hobby'의 value 값과 형태 출력
print(dict1.get('Lang'), type(dict1.get('Lang'))) #'Lang'의 value 값과 형태 출력
print('이름은 ' + dict1.get('Name') + '이며' + ' 나이는', dict1.get('Age'), '입니다.')
print('음악감상' in dict1.get('Hobby')) #'음악감상'이 'Hobby'의 value에 있는지 판단
del dict1['Lang'] #'Lang' key와 그 value 삭제
print('Lang' in dict1) #'Lang' key가 dict1에 있는지 판단
dict1.clear() #dict1 전체 요소 삭제
print(dict1)