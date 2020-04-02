from random import randrange

def game():

    user = int(input("가위 바위 보를 입력하세요 \n"))
    com = randrange(0, 3)

    result = com - user
    result_str = ""

    if com < user :
        com = com + 3

    if result == 2:
        result_str = "이김"
    elif result == 1:
        result_str = "짐"
    else :
        result_str = "비김"

    return result_str

vs_list=[]

for x in range(10):
    result = game()
    vs_list.append(result)

print(vs_list)

