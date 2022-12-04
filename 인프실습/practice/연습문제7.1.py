f_out = open('student.txt', 'w')
student=["김지호", "2020112161", "23", "정보통신공학", "3학년", "01071081291"]
for datas in student:
    f_out.writelines(f'{datas}\n')
f_out.close()

f_in = open('student.txt', 'r')
info = f_in.read()
print(info)
f_in.close()