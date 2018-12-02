# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime, json
# 절대경로 지정
import sys
sys.path.append('/pooh_app')
from parsing import parse
from db import today_menu, tomorrow_menu


# Create your views here.

# 키보드 버튼
def keyboard(request):
    return JsonResponse(
        {
        'type': 'buttons',
        'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
        }
    )

# 오늘 요일이 주말인지 아닌지 검증
def day_search():
    today = datetime.datetime.today()
    weekday_number = today.weekday()
    # 오늘이 토요일인 경우
    if weekday_number == 5:
        return JsonResponse(
            {
                'message': {
                        'text': "토요일은 식당을 운영하지 않습니다."
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                }
            }
        )
    # 오늘이 일요일인 경우
    elif weekday_number == 6:
        return JsonResponse(
            {
                'message': {
                        'text': "일요일은 식당을 운영하지 않습니다."
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                }
            }
        )
    else:
        return 1

# 내일 요일이 주말인지 아닌지 검증
def next_search():
    today = datetime.datetime.today()
    weekday_number = today.weekday()
    # 오늘이 금요일인 경우(즉, 내일이 토요일)
    if weekday_number == 4:
        return JsonResponse(
            {
                'message': {
                        'text': "토요일은 식당을 운영하지 않습니다."
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                }
            }
        )
    # 오늘이 토요일인 경우(즉, 내일이 일요일)
    elif weekday_number == 5:
        return JsonResponse(
            {
                'message': {
                        'text': "일요일은 식당을 운영하지 않습니다."
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                }
            }
        )
    else:
        return 1
       

@csrf_exempt
def message(request):
    # 버튼값 처리
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    button_name = received_json['content']
    # 오늘 날짜
    today = datetime.datetime.today()
    today_date = today.strftime("%Y-%m-%d")
    # 내일 날짜
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_date = tomorrow.strftime("%Y-%m-%d")


# A동 학식(교직원 식당) 버튼
    if button_name == "A동 학식(교직원 식당)":
        if day_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': today_date+"\nA동 학식(교직원 식당)\n\n점심(11:30 ~ 14:00)\n: 5,000원\n-------------------------------------"+today_menu(0)+"\n-------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                    }
                }
            )
        else:
            return day_search()


# B동 학식 버튼
    elif button_name == "B동 학식":
        if day_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': today_date+"\nB동 학식\n\n아침(08:00 ~ 10:00) : 2,900원\n-----------------------------------------------"+today_menu(1)+"\n-----------------------------------------------\n\n\n점심(11:00 ~ 15:30)\n-----------------------------------------------\n"+"3,100 ~ 3,200원"+today_menu(2)+"\n\n3,400 ~ 3,900원"+today_menu(3)+"\n\n3,600 ~ 3,900원"+today_menu(4)+"\n\n4,000원"+today_menu(5)+"\n\n4,100원"+today_menu(6)+"\n\n4,200원"+today_menu(7)+"\n\n4,300원"+today_menu(8)+"\n-----------------------------------------------\n\n\n저녁(17:00 ~ 19:00)\n-----------------------------------------------"+"\n2,600원"+today_menu(9)+"\n\n3,400원"+today_menu(10)+"\n-----------------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                    }
                }
            )
        else:
            return day_search()


# 신기숙사(새로암학사) 식당 버튼
    elif button_name == "신기숙사(새로암학사) 식당":
        if day_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': today_date+"\n신기숙사(새로암학사) 식당\n\n아침(07:30 ~ 09:00)\n: 3,500원\n-------------------------------------"+today_menu(11)+"\n-------------------------------------\n\n\n점심(12:00 ~ 13:30)\n-------------------------------------\n"+"3,100원"+today_menu(12)+"\n\n3,500원"+today_menu(13)+"\n\n3,700원"+today_menu(14)+"\n\n3,900원"+today_menu(15)+"\n-------------------------------------\n\n\n저녁(17:30 ~ 19:00)\n: 3,500원\n-------------------------------------"+today_menu(16)+"\n-------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                    }
                }
            )
        else:
            return day_search()


# 구기숙사(두루암학사) 식당 버튼
    elif button_name == "구기숙사(두루암학사) 식당":
        if day_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': today_date+"\n구기숙사(두루암학사) 식당\n\n아침(07:30 ~ 09:00)\n: 3,500원\n-------------------------------------"+today_menu(17)+"\n-------------------------------------\n\n\n저녁(17:30 ~ 18:55)\n: 3,500원\n-------------------------------------"+today_menu(18)+"\n-------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                    }
                }
            )
        else:
            return day_search()


# 내일 A동 학식(교직원 식당) 버튼
    elif button_name == "내일 A동 학식(교직원 식당)":
        if next_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': tomorrow_date+"\nA동 학식(교직원 식당)\n\n점심(11:30 ~ 14:00)\n: 5,000원\n-------------------------------------"+tomorrow_menu(0)+"\n-------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                    }
                }
            )
        else:
            return next_search()


# 내일 B동 학식 버튼
    elif button_name == "내일 B동 학식":
        if next_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': tomorrow_date+"\nB동 학식\n\n아침(08:00 ~ 10:00) : 2,900원\n-----------------------------------------------"+tomorrow_menu(1)+"\n-----------------------------------------------\n\n\n점심(11:00 ~ 15:30)\n-----------------------------------------------\n"+"3,100 ~ 3,200원"+tomorrow_menu(2)+"\n\n3,400 ~ 3,900원"+tomorrow_menu(3)+"\n\n3,600 ~ 3,900원"+tomorrow_menu(4)+"\n\n4,000원"+tomorrow_menu(5)+"\n\n4,100원"+tomorrow_menu(6)+"\n\n4,200원"+tomorrow_menu(7)+"\n\n4,300원"+tomorrow_menu(8)+"\n-----------------------------------------------\n\n\n저녁(17:00 ~ 19:00)\n-----------------------------------------------"+"\n2,600원"+tomorrow_menu(9)+"\n\n3,400원"+tomorrow_menu(10)+"\n-----------------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                    }
                }
            )
        else:
            return next_search()


# 내일 신기숙사(새로암학사) 식당 버튼
    elif button_name == "내일 신기숙사(새로암학사) 식당":
        if next_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': tomorrow_date+"\n신기숙사(새로암학사) 식당\n\n아침(07:30 ~ 09:00)\n: 3,500원\n-------------------------------------"+tomorrow_menu(11)+"\n-------------------------------------\n\n\n점심(12:00 ~ 13:30)\n-------------------------------------\n"+"3,100원"+tomorrow_menu(12)+"\n\n3,500원"+tomorrow_menu(13)+"\n\n3,700원"+tomorrow_menu(14)+"\n\n3,900원"+tomorrow_menu(15)+"\n-------------------------------------\n\n\n저녁(17:30 ~ 19:00)\n: 3,500원\n-------------------------------------"+tomorrow_menu(16)+"\n-------------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                    }
                }
            )  
        else:
            return next_search()


# 내일 구기숙사(두루암학사) 식당 버튼
    elif button_name == "내일 구기숙사(두루암학사) 식당":
        if next_search() == 1:
            return JsonResponse(
                {
                    'message': {
                            'text': tomorrow_date+"\n구기숙사(두루암학사) 식당\n\n아침(07:30 ~ 09:00)\n: 3,500원\n--------------------------------"+tomorrow_menu(17)+"\n--------------------------------\n\n\n저녁(17:30 ~ 18:55)\n: 3,500원\n--------------------------------"+tomorrow_menu(18)+"\n--------------------------------"
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                    }
                }
            )
        else:
            return next_search()


# 내일 메뉴 버튼
    elif button_name == "내일 메뉴":
        return JsonResponse(
            {
                'message': {
                        'text': '메뉴를 볼 식당을 선택해주세요.'
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', '내일 A동 학식(교직원 식당)', '내일 B동 학식', '내일 신기숙사(새로암학사) 식당', '내일 구기숙사(두루암학사) 식당', '뒤로']
                }
            }
        )


# 뒤로 버튼
    elif button_name == "뒤로":
        return JsonResponse(
            {
                'message': {
                        'text': '오늘 메뉴로 돌아왔습니다.'
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                }
            }
        )


# 도움말 버튼
    elif button_name == "도움말":
        return JsonResponse(
            {
                'message': {
                        'text': "안녕하세요!! 홍익대학교 세종캠퍼스 식단표 챗봇입니다. 이 챗봇은 각 식당의 메뉴들을 알려주며 해당 응답은 홈페이지의 식단표를 기준으로 제작되었습니다.\n\n1. 각 버튼은 오늘 날짜에 해당하는 식당의 메뉴입니다.\n\n2. '내일 메뉴' 버튼을 누르면 내일 날짜의 각 메뉴들을 볼 수 있으며 오늘 메뉴로 돌아오려면 '뒤로' 버튼을 누르시면 됩니다.\n\n3. 금액만 나와 있고 메뉴가 없는 경우는 해당 금액의 메뉴가 없다는 의미입니다.\n\n4. 가끔 버튼이 사라지는 경우가 있습니다. 그런 경우 방을 나갔다가 다시 들어오시면 됩니다.\n\n5. 홈페이지를 기준으로 제작했기 때문에 실제 금액과 다를 수도 있다는 점 양해 바랍니다.\n\n\nP.S : 해당 응답이 홈페이지의 식단표와 다른 경우 저한테 알려주시면 밥이나 커피 한 잔 사드리겠습니다^^"
                 },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['도움말', 'A동 학식(교직원 식당)', 'B동 학식', '신기숙사(새로암학사) 식당', '구기숙사(두루암학사) 식당', '내일 메뉴']
                }
            }
        )
