# BASIC CRUD WITH FLASK

## Create Database
If any changes are made, don't forget to modify connection_db.py
```
mkdir $HOME/crud_flask_db && cd $_
sudo docker run -p 5435:5432 --name crud_db -v $(pwd):/var/lib/postgresql/data -e POSTGRES_PASSWORD=cR7d.@db_s1mp3 postgres
docker start crud_db
docker exec -it crud_db psql -U postgres
CREATE DATABASE crudflask;
CREATE USER crudflask_user with encrypted password 'cR7d.@db_s1mp3';

GRANT ALL PRIVILEGES ON DATABASE crudflask TO crudflask_user;
\q
```

## API - Users
| Url | Method | Description | Params |
| --- | ------ | ----------- | ------ |
| / | Get | Get all users | - |
|  | Post | Add a user | Json with fullname, email  and phone as params  |
| --- | ------ | ----------- | ------ |
| /user | Get | Get one user | User ID |
### Examples
#### Get API
```
curl http://localhost:5006/api/users/user?id=1
```
#### Response
```
{
  "email": "pepito@xyz.com",
  "fullname": "Pedrito Juarez",
  "phone": "987654321"
}
```
#### Post API
```
curl -d '{"fullname":"Pedro Iglesias","phone":"987654321", "email":"pedrito@iglesias.com"}' -H "Content-Type: application/json" http://localhost:5006/api/users
```
#### Response
```
{
  "error": false,
  "message": "User created"
}
```