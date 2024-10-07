import pickle

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
    name = input("name >> ")
    age = input("age >> ")
    addr = input("addr >> ")
    address = Address(name, age, addr)
    addressList.append(address)

def searchAddress():
    "주소 정보 검색"
    print(">>>>>> 주소 검색 처리 >>>>>>")
    name = input("find name >> ")
    for address in addressList:
        if name == address.name:
            print(address)

def searchAllAddress():
    "모든 주소 정보 검색"
    print(">>>>>> 모든 주소 정보 검색 처리 >>>>>>")
    for address in addressList:
        print(address)

def deleteAddress():
    "주소 정보 삭제"
    print(">>>>>> 주소 삭제 처리 >>>>>>")
    name = input("delete name >> ")
    for address in addressList:
        if name == address.name:
            addressList.remove(address)

def updateAddress():
    "주소 정보 수정"
    print(">>>>>> 주소 수정 처리 >>>>>>")
    uname = input("update name >> ")
    for address in addressList:
        if uname == address.name:
            print(address)
            name = input("new name >> ")
            age = input("new age >> ")
            addr = input("new addr >> ")
            address.name = name
            address.age = age
            address.addr = addr
            print(address)

def saveAddress():
    "파일에 주소록 저장"
    print(">>>>>> 주소 저장 처리 >>>>>>")
    # 객체는 text가 아니므로 binary모드인 wb로 저장해야 한다.
    try:
        with open("addressList.bin", "wb") as f:
            pickle.dump(addressList, f)
    except Exception as e:
        print(f"No Saved File: {e}")

def loadAddress():
    "파일로부터 주소록 복원"
    print(">>>>>> 주소 복원 처리 >>>>>>")
    try:
        with open("addressList.bin", "rb") as f:
            global addressList
            addressList = pickle.load(f)
    except Exception as e:
        print(f"No Loaded File: {e}")


def main():
    "프로그램의 시작"
    loadAddress()
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
            saveAddress()
            isRun = False
        else:
            print("잘못 입력!!!")

    print("Program End---")


# 파이썬은 직접 실행할 때 __name__에 __main__값이 저장된다.
# 다른 프로그램에 간접 모듈로 포함될 때는 __name__에 파일명이 저장된다.
if __name__ == '__main__':
    main()