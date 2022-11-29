# Welcome to the Immovable Hutting repository!

This project is an ApiRest that integrates a property search system, with its ads and reservations.

<details>
  <summary><strong>🤷 What was used?</strong></summary><br />

  <strong>Technologies</strong><br />
  ~ Python<br />
  ~ Django<br />
  ~ ORM(Django Rest Framework)<br />
  ~ Data Base(sqlite3)<br />
  ~ Pytest<br />
  ~ Black<br />
  ~ Flake8<br />
</details><br />

<summary><strong>👨‍💻 How it works ?</strong></summary><br />

The application has three APIs, one for Immobles, one for Annoucements and the other for Reserves.

<strong>-> Application APIs</strong> 

- **Immoble**<br />
-present in path 'immovablehutting/models';<br />
-can interact with all http methods;<br />

- **Annoucement**<br />
-present in path 'immovablehutting/models';<br />
-does not interact only with the delete http method;<br />

- **Reserve**<br />
-present in path 'immovablehutting/models';<br />
-does not interact only with update http methods;<br /><br />

# Guidelines<br />

ATTENTION: make sure you have python installed on your machine<br />

<details>
  <summary><strong>Get ready and follow the steps</strong></summary><br />

  ~ create a directory on your machine and access it with the terminal;<br />
  ~ create and access the virtual environment:<br />
    - `python3 -m venv .venv && source .venv/bin/activate` <br />
  ~ install the dependencies:<br />
    - `python3 -m pip install -r requirements.txt` <br/>
  ~ now start the API:<br />
    - `python3 manage.py runserver`
</details><br /><br />

# Consuming the API<br />

![alt text](./runserver.png)<br />
-after starting the application your cmd will be similar to this one where it indicates a port to be accessed (ex: 'http://127.0.0.1:8000/')
