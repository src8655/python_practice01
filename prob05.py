# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

listdata = [0, 1, 5, 6, 11, 15, 50, 70, 88, 89, 90, 91, 100, 150, 156]
print(len(listdata), type(listdata))

list_cnt = 0
list_sum = 0
for i in range(0, len(listdata)):
    if listdata[i] % 3 == 0 and listdata[i] != 0:
        list_cnt += 1
        list_sum += listdata[i]

print('주어진 리스트에서 3의 배수의 개수=>', list_cnt)
print('주어진 리스트에서 3의 배수의 합=>', list_sum)