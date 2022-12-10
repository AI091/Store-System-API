# Store-System-API

The project is currently an Online Store REST-API backend developed in Flask with functionality demonstrated below that is deployed on render.com you can try it here https://e-shop-api-llqs.onrender.com

## Architecture
The API is built following the MVC Pattern where the resource package is the controller layer and the Model package is the Model Layer 

## Functionality
The API is built to be a template extendable E-Commerce API that supports CRUD operations . The ER Diagram is demonstrated here 
![ERD](https://github.com/AI091/Store-System-API/blob/master/Entity-Relationship-Diagram.png)

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
   ├── resources
   │   ├── __init__.py
   │   ├── cart.py
   │   ├── order.py   
   │   ├── store.py	
   │   ├── item.py	
   │   └── tag.py
   │   └── user.py
   ├── .env.example
   ├── .flaskenv
   ├── Dockerfile
   ├── ERD.png
   ├── docker-runner.sh
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
       ├── manage_store.py

```
**app.py** : starting point of the application that runs the API .

**resources/** : The Controller Layer .
- **cart.py** : Contatins end points of operations on cart .
- **order.py** : Contatins end points of operations on orders.  
- **store.py** : Contatins end on managing stores .
- **item.py** : Contatins end points of operations on items. 
- **tag.py** : Contains end points to add tags to stores/items.
- **User.py** : contatins end points manaing user authentication and profile .

**.env.example** : Example of environment file needed to geth the project running  .

**Dockerfile** : text document that can be built into an image with docker to get the project runnning with ease .

**docker-runner.sh **: A script used in the Dockerfile.

**requirements.txt**: Python dependencies 

**schemas.py** : Marshmallow Schemas used for API serialization , deserialization and automatic api-calls validation. 

**models/** : The Model layer of the Project 
- **cart** : cart related table
- **collections** : collections related table
- **item** : items related table
- **item-tags** : Table mapping between items and tags 
- **order** : orders related table
- **tag** : tags table 
- **user** : users table 
- **manage_store** : Mapping between store_managers and stores .

To get a better idea of the database check the ER diagram in the picture aboue.




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


