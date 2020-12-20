# 랜덤 주식 시뮬레이터

import random

initinp = int(input('매수 가격은 얼마인가요?: '))
daysinp = int(input('몇 일 동안 가지고 계실건가요?: '))
timesinp = int(input('몇 번 시뮬레이트 할까요?: '))
dailyMax = 10
dailyMin = -10

# result = init

# for d in range(days-1):
#     ratio = (100+random.randint(dailyMin, dailyMax))/100
#     result *= ratio
#     if d == 0:
#         min = max = result
#     d += 1
#     if result > max:
#         max = result
#     if result < min:
#         min = result
#     if result <= init*0.01:
#         print(f'상장폐지 되었습니다! 깔깔,{d}일 경과')
#         break

# print(f'result:{result:.2f}$\nmin:{min:.2f}$\nmax:{max:.2f}$')


# 평균 구하는 함수
def calcAve(listinp):
    acc=0
    for i in range(len(listinp)):
        acc = acc + listinp[i]
        i = i + 1
    return acc/len(listinp)




def simStock(initPrice, forDays):
    result = initPrice
    profit = 0
    delisted = False

    for d in range(forDays-1):
        ratio = (100+random.randint(-10, 10))/100
        result *= ratio
        if d == 0:
            minp = maxp = result
        d += 1
        if result > maxp:
            maxp = result
        if result < minp:
            minp = result
        if result <= initPrice*0.01:
            delisted = True
            print(f'상장폐지 되었습니다! 깔깔,{d}일 경과')
            break
    profit = ((result/initPrice)-1)*100

    print(f'result:{result:.2f}$\nmin:{minp:.2f}$\nmax:{maxp:.2f}$\nprofit:{profit:.1f}%\n')
    return result, minp , maxp , profit , delisted


def simStockTimes(init,days,times):
    
    resList=[]
    minList=[]
    maxList=[]
    proList=[]
    delCount=0
    earnedCount=0
    
    for t in range(times):
        simResult = simStock(init,days)
        
        if simResult[4] != True:
            resList.append(simResult[0])
            maxList.append(simResult[1])
            minList.append(simResult[2])
            proList.append(simResult[3])
            
            if simResult[3] > 0 :
                earnedCount = earnedCount + 1
        else:
            delCount= delCount + 1
        t =+ 1
        
    aveRes = round(calcAve(resList))
    avePro = round(calcAve(proList))
    earnRate = round(((earnedCount/times)*100))
    
    return aveRes, avePro, delCount , earnRate

aveRes,avePro,delCount,earnRate = simStockTimes(initinp,daysinp,timesinp)

print(f"""일별 등락률:{dailyMin}% ~ {dailyMax}% 
상장 폐지 됐을 경우를 제외했을 때, 입력하신 날짜가 지난 후에 평균 가격은 {aveRes}였습니다.
평균 수익률은 {avePro}% 였으며, 상장폐지 된 횟수는 {delCount}회 입니다. 수익이 났을 확률은 {earnRate}% 입니다.
""")
