sh stop.sh
docker volume rm smart_tracker_backend_postgres_data smart_tracker_backend_pgadmin_data
sh build.sh
sh run.sh
sh migrate.sh