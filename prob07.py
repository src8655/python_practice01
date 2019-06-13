# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

list_data = []
for i in range(0, 5):
    number = input('> ')
    try:
        number = int(number)
    except ValueError:
        print('정수가 아닙니다')
        exit(0)
    list_data.append(number)

print('평균:', sum(list_data)/5)