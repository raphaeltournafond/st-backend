sh stop.sh
docker-compose --env-file ../.env.test -f ../docker-compose.test.yml down
docker volume rm smart_tracker_backend_test_postgres_data
docker-compose --env-file ../.env.test -f ../docker-compose.test.yml up -d --build
docker-compose --env-file ../.env.test -f ../docker-compose.test.yml exec web python manage.py makemigrations
docker-compose --env-file ../.env.test -f ../docker-compose.test.yml exec web python manage.py migrate
docker-compose --env-file ../.env.test -f ../docker-compose.test.yml exec web python manage.py test
docker-compose --env-file ../.env.test -f ../docker-compose.test.yml down