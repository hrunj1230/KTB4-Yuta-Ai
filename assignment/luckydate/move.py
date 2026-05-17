import datetime as dt
from korean_lunar_calendar import KoreanLunarCalendar
# 띠 충돌 데이터

zodiac_conflict = {
    "자": "오",
    "축": "미",
    "인": "신",
    "묘": "유",
    "진": "술",
    "사": "해",
    "오": "자",
    "미": "축",
    "신": "인",
    "유": "묘",
    "술": "진",
    "해": "사"
}
calendar = KoreanLunarCalendar()
today = dt.datetime.today()

def move_getSondate(birthday):
    sonday = []
    user_year = str(birthday)
    calendar.setSolarDate(int(user_year[:4]),int(user_year[4:6]),int(user_year[6:]))
    user_gapja = calendar.getGapJaString()
    user_ganji = user_gapja.split()[-1]
    user_branch = user_ganji[1]

    for i in range(365):
        score = 0
        target = today + dt.timedelta(days = i)
        year , month , day = target.year, target.month, target.day 
        calendar.setSolarDate(year,month,day)
        gapja = calendar.getGapJaString()
        day_ganji = gapja.split()[-1]
        date_branch = day_ganji[1]
        #음력
        lunar = calendar.LunarIsoFormat()
        lunar_day = calendar.lunarDay

        if lunar_day % 10 in [9,0]:
            score +=10
            #print(f"{target.date()}은 손없는 날로 양력{lunar} 입니다.")
        if zodiac_conflict[user_branch] == date_branch:
            score +=10
        if score == 20:
            print(f"{target.date()}가 이사에 좋은 날짜 입니다.")