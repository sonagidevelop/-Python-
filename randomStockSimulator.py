# 랜덤 주식 시뮬레이터

import random

init = int(input('매수 가격은 얼마인가요?: '))
days = int(input('몇 일 동안 가지고 계실건가요?: '))


result = init

for d in range(days-1):
    ratio = (100+random.randint(-10, 10))/100
    result *= ratio
    if d == 0:
        min = max = result
    d += 1
    if result > max:
        max = result
    if result < min:
        min = result
    if result <= init*0.01:
        print(f'상장폐지 되었습니다! 깔깔,{d}일 경과')
        break

print(f'result:{result:.2f}$\nmin:{min:.2f}$\nmax:{max:.2f}$')

