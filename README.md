# Store-System-API

The project is currently an Online Store REST-API backend developed in Flask with functionality demonstrated below that is deployed on render.com you can try it here https://e-shop-api-llqs.onrender.com

## Architecture
The API is built following the MVC Pattern where the resource package is the controller layer and the Model package is the Model Layer 

## Functionality
The API is built to be a template extendable E-Commerce API that supports CRUD operations . The ER Diagram is demonstrated here 
![ERD](https://github.com/AI091/Store-System-API/blob/master/ERD.png)

## Used Technologies: 
- Flask 
- Flask smorest 
- SQLAlchemy ORM (postgresql / sqlite)
- JWT authentication 
- Marshmallow for serialization , deserialization and validation 
- Docker 
- Deployed on render.com with a Postgres data base instance from ElephantSQL 

## Project layout 
```
└── Store-System-API
   ├── app.py
   ├── data.db
   ├── resources
   │   ├── __init__.py
   │   ├── cart.py
   │   ├── store.py	
   │   └── tag.py
   │   └── user.py
   ├── .env.example
   ├── .flaskenv
   ├── Dockerfile
   ├── ERD.png
   ├── docker-unner.sh
   ├── requirements.txt
   ├── schemas.py
   └── models
       ├── init.py
       ├── address.py
       └── cart.py
       ├── collection.py
       ├── item.py
       ├── item_tags.py
       ├── order.py
       ├── store.py
       ├── tag.py
       ├── user.py
```



## To run the project locally : 
After cloning/downloading the project you can get the project running in one of two ways  
### 1- Docker (Recommended) : 
with docker installed on the system run the following 
```
docker build -t "image_name" . 
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" "image_name" -c "flask run --host 0.0.0.0"

```
### 2- Via requirements.txt : 
- create a python virtual environment (optional) , more on that [here](https://docs.python.org/3/library/venv.html)
- install the required dependencies
```
pip install -r requirements.txt
```
- perform database migrations 
```
flask db migrate
flask db upgrade
```
- Run the app using Flask-CLI 
``` 
flask run
```


