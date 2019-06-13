# 문제10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

number = input('숫자를 입력하세요: ')
try:
    number = int(number)
except ValueError:
    print('정수가 아닙니다')
    exit(0)

result = 0
if number % 2 != 0 and number != 0:
    for i in range(0, number+1):
        if i % 2 != 0:
            result += i
else:
    for i in range(0, number + 1):
        if i % 2 == 0:
            result += i
print('결과 값 :', result)