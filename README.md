# Django-Chatbot
이번 프로젝트는 홍익대학교 세종캠퍼스 교내 학식 챗봇으로 오늘의 식당 메뉴 뿐만 아니라 내일의 식당 메뉴까지 확인할 수 있는 챗봇입니다. 이 챗봇은 카카오톡 챗봇이며 Docker Container로 구성되어 있고 카카오톡 플러스 친구에 "hongik_cafeteria"라고 검색하시면 서비스를 이용하실 수 있습니다. <br>하지만 이 API형 챗봇은 카카오 방침에 따라 12월 31일까지만 서비스가 가능하다고 합니다(12월 31일 이후에는 API형이 아닌 카카오 i 오픈빌더를 사용하셔야 합니다). 그래서 이 프로젝트는 12월 31일까지만 유효합니다. <br>해당 파일들을 통해 직접 서비스하고 싶으시다면 git clone을 통해 다운로드 받은 후 install.sh에 실행 권한만 주고 실행하면 됩니다(물론 본인의 설정에 맞게 조금 바꾸셔야 될 수도 있습니다). <br><br>
<img src="https://github.com/P00HP00H/P00HP00H.github.io/blob/master/img/hello1/24.jpg?raw=true" width="300px">

도움말을 누르면 챗봇에 관한 설명이 나오고 아래 버튼들을 보면 각 식당의 메뉴들과 내일 메뉴 버튼이 있습니다.<br>각 식당의 버튼들을 누르면 각 식당의 메뉴들을 확인하실 수 있고 내일 메뉴 버튼을 누르면 내일의 식당 메뉴들을 확인하실 수 있습니다. 먼저 A동 식당을 눌러보겠습니다.<br><br><br>
<img src="https://github.com/P00HP00H/P00HP00H.github.io/blob/master/img/hello1/25.jpg?raw=true" width="300px">

이렇게 오늘 날짜와 가격, 메뉴들이 나오는 것을 확인하실 수 있습니다. 학교 홈페이지에 맞춰서 구성했으므로 가격도 다 표시가 되게끔 하였고, 방학의 경우 기숙사는 식당을 운영하지 않아 홈페이지에 기숙사 메뉴들이 빈 칸으로 처리되어 있기 때문에, 챗봇 역시 빈 칸으로 응답합니다.<br><br><br>
<img src="https://github.com/P00HP00H/P00HP00H.github.io/blob/master/img/hello1/26.jpg?raw=true" width="300px">

현재 글을 작성하고 있는 시점은 방학이므로 이렇게 날짜와 가격은 나오지만 메뉴들은 나오지 않습니다. 이번에는 내일 메뉴 버튼을 눌러보겠습니다.<br><br><br>
<img src="https://github.com/P00HP00H/P00HP00H.github.io/blob/master/img/hello1/27.jpg?raw=true" width="300px">

버튼을 보면 내일 메뉴들로 바뀐 것을 확인하실 수 있습니다. 맨 아래쪽에 "뒤로" 버튼을 누르면 오늘 메뉴로 돌아갑니다. 아까 전에 눌렀던 A동 학식과 비교하기 위해 "내일 A동 학식"을 눌러보면<br><br><br>
<img src="https://github.com/P00HP00H/P00HP00H.github.io/blob/master/img/hello1/28.jpg?raw=true" width="300px">

아까 A동 학식과 다르게 날짜가 바뀌어 있고 메뉴 역시 바뀌어져 있는 것을 확인하실 수 있습니다.<br><br><br>P.S : 그냥 install.sh를 실행하면 Django의 Crontab으로 매 주마다 메뉴들을 업데이트하고, hongik_cafeteria 폴더로 가서 docker-compose up -d --build를 해주게 되면 리눅스의 Crontab 기능으로 매 주마다 업데이트를 하게끔 했는데, 사실 Django의 Crontab 기능 역시 리눅스의 Crontab 기능을 이용하는 것이므로 결국 둘 다 리눅스의 Crontab 기능을 이용하는 것입니다.
