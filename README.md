# SIMPL Business Solutions

## Readme 

### To spin this up:
- create and initialize PostgreSQL database 
- [fork/clone the repo at and cd into it](https://github.com/lxwaru/simpl)

- **create and activate virtual environment**

    - in terminal:

    `python -m venv ./.venv`

    `source .venv/bin/activate`

- **DOWNLOAD DEPENDENCIES**

    - in terminal:

    `pip install -r requirements.txt`

- Initialize Alembic
    - in terminal: 
    
    `alembic init alembic`

- When you initialize Alembic, a file called alembic.ini will be created in the root directory. Line 63 should read something like this: 

    `sqlalchemy.url = {your database address}`

    -edit the parameters to match your database address


- Make sure to add the alembic.ini file to the .gitignore for security.

- create a .env file, and add the following:

    `DATABASE_URL={your database address}`  
    `SECRET_KEY=`

- Generate a secret key by typing the `openssl rand -base64 32` into your terminal, then copy/paste the output and assign it to the SECRET_KEY variable in your .env file

## Spin up the UI

- spin the backend  
terminal: `fastapi dev api/main.py`  
- navigate to the backend GUI  
URL: `http://localhost:8000/docs`

- install frontend dependencies  
terminal: `npm install`  
-  spin the frontend  
terminal: `npm run dev`
- navigate to UI  
URL: `http://localhost:5173`
