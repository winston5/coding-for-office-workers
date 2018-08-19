import random

rock = "바위"
scissors = "가위"
paper = "보"
RSP_List = (rock, scissors, paper)
#리스트나 튜플을 만들 때 문자열 그대로 넣어주기보다 변수로 만들기.
#추후 함수 입력 시 변수로 작성하는게 더 용이함.

win_count = 0
lose_count = 0

while win_count < 3 and lose_count <3:
    # or가 아닌 and로 작성해야만 둘 중 하나라도 3을 넘어가는 것을 막을 수 있음
    user_choice = input("{}, {}, {}: ".format(scissors, rock, paper))
    computer_choice = random.choice(RSP_List)
    if user_choice == computer_choice:
        print("{} vs. {} : 비겼습니다".format(user_choice, computer_choice))
    elif user_choice not in RSP_List:
        print("가위, 바위, 보 중에서 입력해 주세요!")
    elif ((user_choice == rock and computer_choice == scissors)
        or (user_choice == scissors and computer_choice == paper)
        or (user_choice == paper and computer_choice == rock)):
        # 길어질 때는 괄호 사용하여 줄 구분, 작성하기
        win_count = win_count + 1
        print("{} vs. {} : 이겼습니다".format(user_choice, computer_choice))
    else:
        # 이 외 경우는 일일이 조건 나열할 필요 없이 else로 처리
        lose_count = lose_count + 1
        print("{} vs. {} : 졌습니다".format(user_choice, computer_choice))

if win_count == 3:
    print("사용자가 최종 승리하였습니다.")
else:
    print("컴퓨터가 최종 승리하였습니다.")
