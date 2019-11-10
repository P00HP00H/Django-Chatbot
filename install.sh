chmod 700 ./dockerfile/script/*.sh
docker-compose up -d --build
sleep 3s
docker exec djangochatbot_node_1 /bin/bash ./start-dev.sh