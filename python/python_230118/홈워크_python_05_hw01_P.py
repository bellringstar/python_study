# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

day_dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
import calendar
while True:
    ymd = {}
    year = int(input('연도를 입력해 주세요: '))
    if calendar.isleap(year):
        print('윤년입니다. 연도를 다시 입력해주세요.')
        
    else:
        print(calendar.calendar(year))
        month = int(input('월을 입력해 주세요: '))
        days = int(input('일자를 입력해 주세요: '))
        if calendar.weekday(year, month, days) == 0:
            print(f'경고 {day_dict[calendar.weekday(year, month, days)]}입니다.')
        ymd['년'] = year; ymd['월'] = month; ymd['일'] = days
        ymd['요일'] = day_dict[calendar.weekday(year, month, days)]
        print(ymd)
        break




