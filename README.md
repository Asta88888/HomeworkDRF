Проект на Django + Django REST Framework с Docker, PostgreSQL, Redis и Celery.
1. **Клонируем проект**
* bash
* git clone <ссылка-на-репозиторий>
* cd <имя-проекта>

2. Создаём файл .env
* Скопируйте пример и заполните своими значениями: 
* cp .env.example .env

3. Запускаем Docker Desktop
* Убедитесь, что Docker Desktop запущен.

4. Запускаем проект
* docker-compose up --build

5. Проверка работы сервисов

Backend (Django):

http://localhost:8000/

http://localhost:8000/admin/

http://localhost:8000/materials/

http://localhost:8000/users/

Документация API:

Swagger: http://localhost:8000/swagger/

Redoc: http://localhost:8000/redoc/

PostgreSQL: localhost:5432
Redis: localhost:6379

6. Управление Celery
* Запуск воркера:

docker-compose run --rm backend celery -A core worker -l info

* Запуск планировщика задач:

docker-compose run --rm backend celery -A core beat -l info

7. Остановка проекта
* docker-compose down


*Инструкции по настройке удаленного сервера и деплоя.*
1) Создаем виртуальную машину в Yandex Cloud или в Google Cloud или на других ресурсах.
2) Копируем IP виртуальной машины 
3) Вставляем IP виртуальной машины и вносим в Secrets в GitHub, туда же вносим SSH ключ и ключи DOCKER_HUB_USERNAME, DOCKER_HUB_ACCESS_TOKEN
4) Соединяем виртуальную машину с компьютером, и после успешного соединения подтягиваем докер командами: 
* sudo apt-get update
* sudo apt-get install ca-certificates curl
* sudo install -m 0755 -d /etc/apt/keyrings
* sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
* sudo chmod a+r /etc/apt/keyrings/docker.asc
* echo \
   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
   $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
* sudo apt-get update
5) Далее добавляем файрвол(если не активирован) командами:
* sudo ufw status
* sudo ufw enable
* sudo ufw allow 80/tcp
* sudo ufw allow 443/tcp
* sudo ufw allow 22/tcp
6) После запускаем сайт по IP адресу виртуальной машины 158.160.197.44:80
