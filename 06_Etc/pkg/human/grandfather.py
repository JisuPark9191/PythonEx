
class cgrandfather:
    '할아버지 클래스'
    def __init__(self, name:str, age:int, money:int) -> None:
        self.name = name
        self.age = age
        self.money = money

    def intro(self) -> None:
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'money: {self.money}')

    def happy(self) -> None:
        print(f'돈 {self.money}으로 인생이 행복하다~')