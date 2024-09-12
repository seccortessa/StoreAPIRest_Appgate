# StoreAPIRest_Appgate
This repository contains an APIRest developed on FastAPI that allows querying the product's prices of a store, based on several parameters such as application date, product ID, brand ID, etc.



On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.



## Requirements

Please make :

- **Python 3.10+**
- **Docker** (optional, if you want to contenerize the app)

### Project clone


    git clone https://github.com/seccortessa/StoreAPIRest_Appgate.git
    cd StoreAPIRest_Appgate

### Installation method 1 (Locally - for linux)

1. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate  # On Linux/MacOS
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Create the database
```create_db.py``` must be executed one single time.
```
python create_db.py
```
4. Run the server
```
uvicorn app.main:app --reload
```
This will start the server at http://127.0.0.1:8000.



### Installation method 2 (Using Docker - suitable for Windows and Linux)
1. Create the database
```create_db.py``` must be executed one single time.

2. With Docker installed, build the container
```
docker build -t storeapirest .
```
This will set up all dependencies

3. run the app
```
docker run -p 8000:8000 storeapirest
```
The server will be located at http://localhost:8000

### Testing 

Tests are available, use the following command

```
PYTHONPATH=./ pytest  # if running locally (linux)
# or
docker run -e PYTHONPATH=./ fastapirest pytest # if contenerized 
```

### Project Structure

```
StoreAPIRest_Appgate/
│
├── app/
│   ├── __init__.py          
│   ├── main.py              # Definition of the API endpoints 
│   ├── database.py          # Database structuration and configuration
│   ├── dependencies.py      # common dependencies
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database access functions
│   ├── routes.py            # Specific route to endpoint
│
├── tests/
│   ├── __init__.py          
│   └── test_routes.py       # Tests for the routes/endpoint
│
├── create_db.py             # Script to create the database and insert the initial data
├── data.py                  # Data to initialize the database 
├── requirements.txt         # Depencencies
├── arch_definition.txt      # Design and architecture brief description
└── readme.md                # Documentation


```

