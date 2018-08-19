class School:
    def __init__(self,name,year,address): #3가지 데이터를 반드시 입력하도록 입력인자 설정
        self.name = name
        self.year = year
        self.address = address
    def print_school(self): #객체/인스턴스 정보를 한번에 볼 수 있는 print_school 기능 추가
        print("Name: {}, Year: {}, Address: {}".format(self.name, self.year, self.address))

a = School("Seoul","1900","Gwanak")
b = School("JoongAng", "1920", "Sangdo")
c = School("Ehwa", "1890", "Shinchon")
d = School("Hanyang", "2000") #입력인자 하나가 누락됐을 경우 에러가 나는지 확인하기 위함

print(a.name)
print(b.name)
print(c.name)
print(a.year)
print(b.year)
print(c.year)
print(a.address)
print(b.address)
print(c.address)
a.print_school()
b.print_school()
c.print_school()
d.print_school() #에러가 나는지 확인
