from .father import cfather

class cme(cfather):
    "나 클래스"
    def __init__(self, name: str, age: int, money: int, knowledge: str, power) -> None:
        super().__init__(name, age, money, knowledge)
        self.power = power

    def intro(self) -> None:
        super().intro()
        print(f'power: {self.power}')

    def health(self) -> None:
        print(f'{self.power}를 들기 위해 운동을 한다.')

