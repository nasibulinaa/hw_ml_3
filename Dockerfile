FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG MODEL_VERSION=v1.0.0
ENV MODEL_VERSION=${MODEL_VERSION}
ENV MODEL_PATH=iris_model_${MODEL_VERSION}.joblib
COPY app/ .
COPY models/iris_model_${MODEL_VERSION}.joblib iris_model_${MODEL_VERSION}.joblib
EXPOSE 8080
CMD ["python", "app.py"]