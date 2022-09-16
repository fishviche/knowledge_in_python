# BASIC CRUD WITH FLASK

## Create Database

```
mkdir $HOME/crud_flask_db && cd $_
sudo docker run -p 5435:5432 --name crud_db -v $(pwd):/var/lib/postgresql/data -e POSTGRES_PASSWORD=cR7d.@db_s1mp3 postgres
docker start crud_db
docker exec -it crud_db psql -U postgres
CREATE DATABASE crudflask;
CREATE USER crudflask_user with encrypted password 'cR7d.@us3r';
GRANT ALL PRIVILEGES ON DATABASE crudflask TO crudflask_user;
\q
```