def googoodan():
    dan = int(input("몇 단을 출력하시겠습니까?"))
    if 1 < dan < 10:
        for num in range(1,10):
            print("{} x {} = {}".format(dan, num, dan*num))
    else:
        print("2에서 9 사이의 숫자만 입력해 주세요.")
        googoodan()

googoodan()
