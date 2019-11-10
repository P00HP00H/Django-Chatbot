from bs4 import BeautifulSoup
import requests, json


## HTTP GET Request
# 학식 메뉴 크롤링
def parse(a):
    req = requests.get('http://sj.hongik.ac.kr/site/food/food_menu.html')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    food_menu = soup.select(
        'div[class=foodmenu]'
        )
    b = json.dumps(food_menu[a].text)
    return b
