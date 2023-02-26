
FROM postgres:9.3
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 1234
ENV POSTGRES_DB postgres
ADD db/create_tables.sql /docker-entrypoint-initdb.d/

FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY . .

WORKDIR .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "api.user_api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]