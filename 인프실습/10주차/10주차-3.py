f_in = open('attendance.txt', 'r') #'attendance.txt' 파일 읽기
f_out = open('newattendence.txt', 'w') #'newattendance' 파일 생성 및 작성

sum = 0
count_late = 0
count_abs = 0
stu_list = []

f_out.writelines('[출석부:'+f_in.readline().strip()+']\n') #첫 줄 작성

for line in f_in:
    sum += 1 #학생 수 세기
    line_list = line.strip().split("/") #line_list에 "/"로 나누어 넣음
    if line_list[3] == '지각':
        count_late += 1 #지각한 학생 수 증가
        stu_list.append(f'\'{line_list[0]}\' 학생은 <지각> 입니다.') #stu_list에 지각한 학생이 있는 줄 삽입
    elif line_list[3] == '결석':
        count_abs += 1 #결석한 학생 수 증가
        stu_list.append(f'\'{line_list[0]}\' 학생은 <결석> 입니다.') #stu_list에 결석한 학생이 있는 줄 삽입

f_out.writelines(f'총원:{sum}명    지각:{count_late}    결석:{count_abs}\n')
for i in stu_list: #지각, 결석한 학생 'newattendance.txt' 파일에 작성
    f_out.writelines(f'{i}\n')
