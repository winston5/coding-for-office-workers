def gugudan():
    try:
        dan = int(input("2와 9 사이의 숫자를 입력해 주세요: "))
        if dan > 1 and dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan*num))
        else:
            print("2와 9 사이의 숫자만 입력해 주세요!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해 주세요.")
        gugudan()
    except:
        print("알 수 없는 에러가 발생하였습니다.")
        gugudan()

gugudan()
