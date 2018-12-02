# 매주 일요일/월요일 0시 0분에 db.sh 실행
cat <(crontab -l) <(echo "0 0 * * 0,1 /db.sh") | crontab -
python manage.py migrate && python manage.py runserver 0.0.0.0:8000
