# standup_bot
### set crontab
* * * * * source /Users/nnsviridov/PycharmProjects/AcademicProjects/standup_bot/venv/bin/activate && python /Users/nnsviridov/PycharmProjects/AcademicProjects/standup_bot/cron_reminder.py
### Сборка образа из докерфайла и его публикация
docker build -t luchanos/standup_bot:1.0.0 . - собираем (не забываем точку в конце)
docker push luchanos/standup_bot:1.0.0 - пушим в репозиторий
docker pull luchanos/standup_bot:1.0.0 - стаскиваем образ из хаба
docker run luchanos/standup_bot:1.0.0 - запускаем контейнер с ботом
docker exec -it 72175d2b7af1 sh

Для установки sudo:
RUN apt-get update && apt-get -y install sudo
Аналогично можно установить всё остальное, например crontab.

Для запуска бота в фоновом режиме:
supervisor, который мы ставим в venv и потом после активации можем пользоваться.

Чтобы искать процессы:
ps -ef | grep supervisord

Чтобы убивать процессы:
kill -s SIGTERM 16680