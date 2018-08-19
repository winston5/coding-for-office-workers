##### 1. 사람 클래스 만들기
# 사람 기본 요소: 이름, 나이, 성별
# 힌트2: 사람의 기본 요소 (이름, 나이, 성별)은 각각 새로운 사람 만들 때 입력 받을 수 있도록 함
class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_contact(self):
        print('이름: {}'.format(self.name))
        print('나이: {}'.format(self.age))
        print('성별: {}'.format(self.gender))

# 객체 생성
contact1 = Person("김민수","25","남")
contact2 = Person("김민아","28","여")

# 출력 확인
print("===사람 클래스===")
print(contact1.name)
print(contact2.age)
contact1.show_contact()

##### 2. 직장 동료 클래스를 사람 클래스를 이용하여 만들기.
# 직장 클래스 별도 요소는 직급
# 힌트1: 클래스와 상속을 활용
# 힌트3: 직장 동료 기본 직급은 "대리"로 지정
class Work1(Person):
    position = "대리"

# 객체 생성
contact3 = Work1("손흥민","25","남")

# 출력 확인
print("===직장 동료 클래스1===")
print(contact3.name)
print(contact3.position)
contact3.show_contact()

##### 3. 고급: 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경을 도전
class Work2(Person):
    def __init__(self, name, age, gender, position):  # 사용할 입력인자 모두 나열
        super().__init__(name, age, gender)  # BaseClass에서 가져올 입력인자를 super()로 참조
        self.position = position  # 새로 추가한 입력인자를 정의
    def show_contact(self):
        super().show_contact()
        print('직급: {}'.format(self.position))

# 객체 생성
contact4 = Work2("이승우","21","남","부장")

# 출력 확인
print("===직장 동료 클래스2===")
print(contact4.name)
print(contact4.position)
contact4.show_contact()
