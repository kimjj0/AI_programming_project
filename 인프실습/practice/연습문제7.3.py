f_in = open("practice7_3.txt", "r")
datas = f_in.readlines()
str_data = str(datas[0])
str1 = input('찾고 싶은 문자열 : ')
if str_data.find(str1) == -1:
    print("없음")
    False
else:
    print("있음")
    True
f_in.close()