# Synthetic index

Module to obtain and insert synthetic index data based on two different securities.

## Introduction

A Flask app has been created to calculate the index value based on the current database data. It is also able to process the data from external processes and insert it into the database.

We have used MySQL8 for the database.

Docker and docker-compose have been used to deploy the system.


<br>


## Flask App

### Endpoints

#### GET /indexes/synthetic

Obtains the time series of the index value for the current date. 
Sample response:
```json
{
    "values": [
        120.1,
        123.4,
        133.4
    ]
}
```



#### POST /indexes/synthetic/data

Inserts security data into the database. This endpoints is available for public and private resources to insert data that will be used to calculate the index. 

Sample body ('application/json'):

```json
{
    "values": [
        {
            "id_security": 1,
            "price": 127
        },
        {
            "id_security": 2,
            "price": 247
        }
    ]
}
```

<br>

### Deploy

We have used gunicorn and gevent to handle a future production environment. We could set the number of workers at the `wsgi.py` file using a environment variable or the config file.

<br>

### TO DO

* Cache index per date
* Add swagger documentation
* Profile speed of data retrieval from database and calculus
* Improve POST to be more intuitive for external apps

<br>


## SQL

We have created a database model (model.mwb) that can be opened using MySQL Workbench. It includes two tables:

* Security: id_security, name, weight. For each security we have a weight as described in the document.

* Security_price: id_security_price, id_security, price, date. For each security we have multiple prices correspondent to dates. We have to handle multiple prices per date, using the last one.

Scripts in "sql_init_data" folder are using for the docker deployment explained in the next section to apply at the database initialization.

We have used a basic set of data to test the system.


<br>

## Docker

To deploy the database and the app we have used docker-compose. The template file is `docker-compose.yaml`:

```yaml
version: "3.7"
services:
  db:
    image: mysql:8.0.15
    ports:
      - "32000:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: wealth
    volumes:
      - ./sql_init_data:/docker-entrypoint-initdb.d/:ro
      - sql_data:/var/lib/mysql_db
    command: mysqld --default-authentication-plugin=mysql_native_password --skip-mysqlx
    container_name: mysql_db
  flask:
    build: ./flask-app
    container_name: flask
    environment:
      - APP_NAME=MyFlaskApp
      - API_PORT=3000
    expose:
      - 3000
    ports:
      - "3000:3000"
  
volumes:
  sql_data:
```

### TO DO

* Improve Flask App docker image size
* Flask database credentials

##  Run

Run in a shell terminal:

```bash
docker-compose up -d
```

Then the application will be deployed at [http://localhost:3000/](http://localhost:3000/)

To get data use http://localhost:3000/indexes/synthetic

To send data use http://localhost:3000/indexes/synthetic/data