text = input('今日は何をした？ >>')
with open('diary.txt','a')as file:
    file.write(f'{text} \n')