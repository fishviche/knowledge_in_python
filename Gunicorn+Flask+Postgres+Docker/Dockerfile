FROM python:3.9
RUN apt-get update
RUN mkdir /app
COPY . /app
WORKDIR /app
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV DB_USERNAME="crudflask"
ENV DB_PASSWORD="cR7d.@us3r"
ENV DB_HOST="crud_db"
RUN pip install --no-cache-dir -r requirements.txt