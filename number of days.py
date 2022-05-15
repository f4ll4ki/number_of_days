def date_count(date):
    year = int(date[0:4])
    month = int(date[4:6])
    day =  int(date[6:8])
    year_cnt=(year-1)*365 + (year-1)//4 - (year-1)//100 +(year-1)//400
    month_cnt = 0
    for mon in range(1,month):
        if mon == 2:
            if year//400 == 0:
                month_cnt += 29
            elif year//100 == 0:
                month_cnt += 28
            elif year//4 ==0:
                month_cnt +=29
            else:
                month_cnt +=28
        elif mon in [1,3,5,7,8,10,12]:
            month_cnt +=31
        else:
            month_cnt +=30
    return year_cnt+month_cnt+day

def main():
    print('날짜 작성 예시: 20210101')
    date1 = input('태어난 날짜 :')
    date2 = input('현재 날짜 :')
    print(abs(date_count(date1)-date_count(date2)),'일')

main()
