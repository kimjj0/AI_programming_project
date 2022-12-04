dict = {'James': 94, 'John': 79, 'Tomas': 46, 'Bob': 60}
name_list = list(dict.keys())
grade_list = list(dict.values())
for i in range(4):
    if grade_list[i] > 80:
        print(f'{name_list[i]}의 성적은 A입니다.')
    elif grade_list[i] > 60:
        print(f'{name_list[i]}의 성적은 B입니다.')
    elif grade_list[i] > 40:
        print(f'{name_list[i]}의 성적은 C입니다.')
    elif grade_list[i] > 20:
        print(f'{name_list[i]}의 성적은 D입니다.')
    else:
        print(f'{name_list[i]}의 성적은 F입니다.')


