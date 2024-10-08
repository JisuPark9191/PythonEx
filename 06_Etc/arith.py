# 변수앞에 *를 붙이면 '가변 인자'라는 의미
# '가변 인자' : 갯수를 정하지 않고 다수의 인자를 받을 수 있다 -> tuple로 전달된다

PI = 3.141592

def add(*args):
    '더하기'
    num = 0
    for i in args:
        num += i
    return num

def sub(*args):
    '빼기'
    num = args[0]
    for i in range(1, len(args)):
        num -= args[i]
    return num

def mul(*args):
    '곱하기'
    num = 1
    for i in args:
        num *= i
    return num

def div(*args):
    '나누기'
    num = args[0]
    for i in range(1, len(args)):
        num /= args[i]
    return num

if __name__ == '__main__':
    print(add(1, 2, 3))
    print(sub(1, 2, 3))
    print(mul(1, 2, 3))
    print(div(1, 2, 3))
    print(f'arith.py에서 직접 실행시 __name__의 값 : {__name__}')
else:
    print(f'다른 파일에서 arith.py를 모듈로 import했을 때 __name__의 값 : {__name__}')
