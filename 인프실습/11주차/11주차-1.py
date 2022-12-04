with open('song.txt', 'r') as f_in: #song.txt 파일을 읽어옴
    datas = f_in.readlines() #파일에 있는 내용을 한줄 씩 datas 변수에 저장
    with open('song_rc.txt', 'w') as f_out: #song_rc.txt 파일을 쓰기 모드로 불러옴
        for line in datas[::-1]: #datas의 내용을 인덱스를 반전시켜 반복
            if line[0] == True:
                f_out.writelines(line)
                break
            f_out.writelines(line)

