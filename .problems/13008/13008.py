"""
    입력은 input() 함수로 받을 수 있어요.
    대신 모든 입력은 문자로 들어옵니다. 123을 입력해도 "123"이라는 문자로 들어와요.
    그래서 int()를 사용해서 숫자로 바꿔줘야 합니다. int(input()) 이렇게요.
"""

# 첫번째 입력받은 값을 x에 저장합니다.
x = input()

# 두번째 입력받은 값을 숫자로 바꿔서 y에 저장합니다.
y = int(input())

# x는 그대로 출력합니다.
print(x)

# y는 10을 곱해서 출력합니다. int()를 이용하여 숫자로 바꿨기 때문에 계산이 가능해요!
print(y*10)
