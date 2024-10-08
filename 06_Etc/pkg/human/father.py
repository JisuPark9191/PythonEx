from .grandfather import cgrandfather

class cfather(cgrandfather):
    '아버지 클래스'
    def __init__(self, name: str, age: int, money: int, knowledge: str) -> None:
        super().__init__(name, age, money)
        self.knowledge = knowledge

    def intro(self) -> None:
        super().intro()
        print(f'knowledge : {self.knowledge}')

    def study(self) -> None:
        print(f'{self.knowledge}를 얻기 위해 공부를 한다')