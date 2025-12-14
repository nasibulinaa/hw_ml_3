HW_ML_3
=======

Демонстрационный проект ML-сервиса со стратегией развертывания модели.

Структура проекта:
```
hw_ml_3/
 ├── app/
 │    └── app.py
 ├── models/
 │    ├── iris_model_v1.0.0.joblib
 │    └── iris_model_v1.1.0.joblib
 ├── requirements.txt
 ├── Dockerfile
 └── README.md
```

## Команды сборки и запуска

### Локальная машина

Сборка и запуск на локальной машине (linux):

```bash
# Установка python-зависимостей
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
# Генерация ML-моделей
./contrib/prepare_dir.sh
# Запуск сервера
python3 app/app.py
# Отправка запросов для теста (другой терминал)
./utils/test_req.sh
```

### Контейнер

Сборка и запуск контейнера:

```bash
# Сборка
docker build -t ml-service:v1 .
# Запуск
docker run --rm -p 8080:8080 ml-service:v1
# Отправка запросов для теста (другой терминал)
./utils/test_req.sh
```

### Примеры вызовов /health и /predict

Отправка запросов:

![](docs/Code_nBB6elxZNl.png)

### Скриншоты вывода команд после запуска контейнера

Сборка и запуск контейнера:

![](docs/Code_AEzI42oY7r.png)


### Реализация стратегии развертывания

Вариант A — Blue-Green Deployment.

