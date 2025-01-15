```
Alex: I made some changes to this README. It's not exhaustive or perfect but should give a basic idea re: direction for what a cleaned up README generally looks like.

Some changes I made directly but there are other things which I summarized as questions or comments with `joecomment: XXXXXXXXXX`

Don't merge my changes, just copy this doc, implement the changes on your own branch and then delete the joes-readme-feedback branch.

Once the README is shaped up and local dev instructions are clarified, I'll spin it up locally and provide more feature- and code-centeric feedback.

```

# SIMPL Business Solutions `joecomment: name this with more specificity...like exactly what does the SIMPL platform *do*`

`joecomment: add a Dependencies section so I know right at the outset what I need to download...looks like I need python (which version?), pip, alembic, openssl, fastapi, npm`

## Local Dev

`joecomment: ### Setup environment`

1. create and initialize PostgreSQL database `joecomment: how do I do this? If it's simple, give a code snippet here. If it's complex, provide a link to exactly where it tells you how to do it.`

2. [fork/clone the repo at and cd into it](https://github.com/lxwaru/simpl)

3. **Create and activate virtual environment**

`$ python -m venv ./.venv`

`$ source .venv/bin/activate`

4. **Download backend dependencies**

`$ pip install -r requirements.txt`

5. Initialize Alembic

`$ alembic init alembic`

When you initialize Alembic, a file called alembic.ini will be created in the root directory. Line 63 should read something like this:

`sqlalchemy.url = {YOUR_DB_ADDRESS}` `joecomment: is this a the connection string?`

Make sure to edit the parameters to match your database address.

Add the alembic.ini file to the .gitignore for security.

6. Create a .env file, and add the following:

`DATABASE_URL={YOUR_DB_ADDRESS}` `joecomment: is this the connection string?`

7. Generate a secret key by typing the `openssl rand -base64 32` into your terminal, then copy/paste the output and assign it to the SECRET_KEY variable in your .env file

`SECRET_KEY={OPENSSL_SECRET_KEY}`

### Run the app

#### Initialize the API

Start the server: `$ fastapi dev api/main.py`

Navigate to the backend GUI: `http://localhost:8000/docs`

#### Initialize the client

Install client dependencies: `$ npm install`

Initialize the frontend: `$ npm run dev`

Navigate to UI: `http://localhost:5173`
