# standup_bot
### set crontab
* * * * * source /Users/nnsviridov/PycharmProjects/AcademicProjects/standup_bot/venv/bin/activate && python /Users/nnsviridov/PycharmProjects/AcademicProjects/standup_bot/cron_reminder.py
### Сборка образа из докерфайла и его публикация
docker build -t luchanos/standup_bot:1.0.0 . - собираем (не забываем точку в конце)
docker push luchanos/standup_bot:1.0.0 - пушим в репозиторий
docker pull luchanos/standup_bot:1.0.0 - стаскиваем образ из хаба
docker run luchanos/standup_bot:1.0.0 - запускаем контейнер с ботом
docker exec -it 72175d2b7af1 sh