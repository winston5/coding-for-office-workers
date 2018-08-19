# 사용자에게 가위, 바위, 보 중 하나를 물어본다.
# 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고, 승패를 가른다.
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 난다.
# 힌트1: 리스트 한 개 사용
# 힌트2: 사용자 입력 받기
# 힌트3: 임의 뽑기 사용. 검색 키워드: random, randint, shuffle
# 힌트4: 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 함

import random

game = ["가위", "바위", "보"]
user_win = 0
computer_win = 0
draw = 0

while (user_win < 3 and computer_win < 3):
    user = input("가위, 바위, 보 중 한 가지를 입력하세요: ")
    print("사용자: {}".format(user))
    number = random.randint(0,2)
    computer = game[number]
    print("컴퓨터: {}".format(computer))

    if user == "가위":
        if computer == "가위":
            draw += 1
        if computer == "바위":
            computer_win += 1
        if computer == "보":
            user_win += 1

    if user == "바위":
        if computer == "바위":
            draw += 1
        if computer == "보":
            computer_win += 1
        if computer == "가위":
            user_win += 1

    if user == "보":
        if computer == "보":
            draw += 1
        if computer == "가위":
            computer_win += 1
        if computer == "바위":
            user_win += 1

    print("사용자: {} vs 컴퓨터: {}".format(user_win, computer_win))
print("게임끝!")
