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
