# docker_backend_plants

## Первый запуск
```
docker-compose up -d --build
```

## Остановка
```
docker-compose down
```

## Повторный запуск

В файле docker-compose.yml для контейнера add_db оставить только команду sleep 7:
```
add_db:
  build:
    context: .
    dockerfile: Dockerfile
  container_name: backend_seed_db
  env_file:
    - .env
  volumes:
    - .:/app
  depends_on:
    - migrate
  command: sh -c "\
    sleep 7"
```
После этого запустить контейнеры
```
docker-compose up
```

## Просмотр логов из api (контейнер web)
```
sudo docker-compose logs -f web
```
