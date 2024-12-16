FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install cython

RUN pip install --upgrade pip setuptools wheel

RUN pip install apache-airflow==2.2.3 --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-3.9.txt

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN airflow db init

RUN airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --email admin@example.com \
    --role Admin \
    --password admin123

EXPOSE 8080

CMD ["airflow", "scheduler"]