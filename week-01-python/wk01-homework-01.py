#처음 파일 실행 시, 한식, 중식, 일식 중 한 가지를 고르라는 내용 출력
#그 중 한 가지 고르면, 식당 이름을 하나 임의로 추천
#힌드: 사용자 입력을 받아야 함
#힌트: 리스트를 여러개 사용

import random

한식 = ["을밀대", "기와집순두부", "평가옥"]
중식 = ["웨스턴차이나", "베이징덕", "취향"]
일식 = ["쥬안", "지구당", "미카도스시"]

user_choice = input("한식, 중식, 일식 중 한 가지를 고르세요.")
if user_choice == "한식":              #따옴표 치고 적어야 사용자가 입력하는 "한식" 문자열과 일치. 따옴표 없으면 리스트.
    choice_result = random.choice(한식)
elif user_choice == "중식":
    choice_result = random.choice(중식)
elif user_choice == "일식":
    choice_result = random.choice(일식)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 합니다.")

if choice_result:
    print("추천 드리는 식당은 {}입니다".format(choice_result))
