

addressList = []        # Address객체를 저장할 전역 리스트 저장소

class Address:
    "주소 정보를 담는 클래스"
    def __init__(self, name, age, addr) -> None:
        self.name = name
        self.age = age
        self.addr = addr
    def __str__(self) -> str:
        "java에서는 ToString()에 해당하는 함수"
        return f'name={self.name}, age={self.age}, addr={self.addr}'

def showMenu():
    "메뉴 보여주기"
    print("\n\n")
    print(f"{'*'*10} Menu {'*'*10}")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Update")
    print("5. SearchAll")
    print("6. Exit")

def getSelectMenu():
    "메뉴 번호 선택"
    return input("select Menu Number >> ")

def insertAddress():
    "주소 정보 입력/저장"
    print(">>>>>> 주소 입력 처리 >>>>>>")
    pass

def searchAddress():
    "주소 정보 검색"
    print(">>>>>> 주소 검색 처리 >>>>>>")
    pass

def searchAllAddress():
    "모든 주소 정보 검색"
    print(">>>>>> 모든 주소 정보 검색 처리 >>>>>>")
    pass

def deleteAddress():
    "주소 정보 삭제"
    print(">>>>>> 주소 삭제 처리 >>>>>>")
    pass

def updateAddress():
    "주소 정보 수정"
    print(">>>>>> 주소 수정 처리 >>>>>>")
    pass

def saveAddress():
    "파일에 주소록 저장"
    print(">>>>>> 주소 저장 처리 >>>>>>")
    pass

def loadAddress():
    "파일로부터 주소록 복원"
    print(">>>>>> 주소 복원 처리 >>>>>>")
    pass

def main():
    "프로그램의 시작"
    isRun = True
    while isRun:       
        showMenu()
        num = getSelectMenu()
        if num == "1":
            insertAddress()
        elif num == "2":
            searchAddress()
        elif num == "3":
            deleteAddress()
        elif num == "4":
            updateAddress()
        elif num == "5":
            searchAllAddress()
        elif num == "6":
            isRun = False
        else:
            print("잘못 입력!!!")

    print("Program End---")


# 파이썬은 직접 실행할 때 __name__에 __main__값이 저장된다.
# 다른 프로그램에 간접 모듈로 포함될 때는 __name__에 파일명이 저장된다.
if __name__ == '__main__':
    main()