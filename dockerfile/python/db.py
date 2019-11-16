import datetime, json, redis
# 절대 경로 지정
import sys
sys.path.append('/pooh_app')
from parsing import parse

# Redis DB 생성 및 연결
r = redis.Redis(host="redis", port=6379, db=0)

# 크롤링한 학식 메뉴들을 Redis에 저장
def menu_insert():
    for i in range(0, 84):
        r.set(i, parse(i))

# 오늘 메뉴를 DB에서 불러오는 함수
def today_menu(a):
    today = datetime.datetime.today()
    weekday_number = today.weekday()
    food_data = r.get(6*a+weekday_number).decode('utf-8')
    food_menu = json.loads(food_data)
    return food_menu

# 내일 메뉴를 DB에서 불러오는 함수
def tomorrow_menu(a):
    today = datetime.datetime.today()
    weekday_number = today.weekday()
    # 해당 요일이 일요일인 경우 다음날인 월요일은 숫자가 다시 0으로 되기 때문에 월요일 식단을 가져오도록 구성
    if weekday_number == 6:
        monday_food_data = r.get(6*a).decode('utf-8')
        monday_food_menu = json.loads(monday_food_data)
        return monday_food_menu
    # 다른 요일들의 다음날은  해당 요일의 숫자에 +1만 해주면 됨
    else:
        food_data = r.get(6*a+(weekday_number+1)).decode('utf-8')
        food_menu = json.loads(food_data)
        return food_menu
