# 문제6.
# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전,
# 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

# /5 /2 /5 /2 /5 /2 /5 /2 /5

number = input('금액: ')
try:
    number = int(number)
except ValueError:
    print('정수가 아닙니다')
    exit(0)

money = 50000
div = 5
for i in range(0, 10):
    mod = number // money
    number -= (mod * money)
    print(int(money), '원 : ', int(mod), '개')

    money /= div
    if div == 5:
        div = 2
    else:
        div = 5