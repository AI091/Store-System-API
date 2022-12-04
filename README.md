# Store-System-API

The project is currently an Online Store REST-API backend developed in Flask with functionality addressed below. 

## Architecture
The API is built following the MVC Pattern where the resource package is the controller layer and the Model package is the Model Layer 

## Used Technologies: 
- Flask 
- Flask smorest 
- SQLAlchemy ORM (postgresql / sqlite)
- JWT authentication 
- Marshmallow for serialization , deserialization and validation 

## Features 
- Dockerizedd 
- Heroku deploayble "yet to be implementedd" 

## DataBase ER diagram : 
![ERD](https://github.com/AI091/Store-System-API/blob/master/ERD.png)





## To run the project : 
You can run the app using two ways : 
### 1- Docker :: yet to be documented 
### 2- Installing the dependiciess : 
It's recommended to setup a virtual enviroment first for isolation the clone/download the repo and insstall dependies using 
```
pip install -r requirements.txt
```
### Run the app 
``` 
flask run
```

### perform database migrations 
```
flask db migrate
flask db upgrade
```



