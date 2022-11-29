# Welcome to the Immovable Hutting repository!

This project is an ApiRest that integrates a property search system, with its ads and reservations.

<details>
  <summary><strong>🤷 What was used?</strong></summary><br />

  <strong>Technologies and Skills</strong><br />
  ~ Python<br />
  ~ Django<br />
  ~ ORM(Django Rest Framework)<br />
  ~ SQL Data Base(sqlite3)<br />
  ~ Pytest<br />
  ~ Black<br />
  ~ Flake8<br />
  ~ Seeders(fixture)<br />
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

ATTENTION: make sure you have python installed on your machine and stay tuned with the version.<br />

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

-After starting the application, your cmd will look like the one in the image below, where it indicates a port to be accessed (eg: 'http://127.0.0.1:8000/').
It is through her that we will carry out the requests.<br />
-Requests will be made from the `/api` route. ex.: http://127.0.0.1:8000/api/ .<br />
-If you don't have a client (such as 'Insomnia, Postman' or any other) installed on your machine, you can carry out the requests through your browser by placing the mouse cursor over the route and pressing 'Ctrl + click' .<br />
-The APIs always returned <strong>Json</strong><br />
![](./runserver.png)<br />

### 🕵 Sample requests will be implemented with the Postman client. <br />

## Routes<br />
 `/api`:<br />
  - `http://127.0.0.1:8000/api/`<br />
  -This route generates the application's API routes through the GET method.<br /><br />
  ![alt text](./req_and_res_images/route_api/getapi.png)<br />
  ![alt text](./req_and_res_images/route_api/responseapi.png)<br />


 `/immobles`:<br />
  - `http://127.0.0.1:8000/api/immobles/`<br />
  -This route interacts with the HTTP methods of a CRUD.<br />
  ![alt text](./req_and_res_images/route_immobles/immobles.png)<br />
  ![alt text](./req_and_res_images/route_immobles/allimmobles.png)<br />
  -For the Post, Put or Patch methods, use the following scope in the client's body:<br />
  ![alt text](./req_and_res_images/route_immobles/bodyexemple.png)<br />
  ```python
  {
    "title": "Home in Miami",
    "immoble_code": 20220017,
    "guest_limit": "2",
    "number_of_bathorroms": 1,
    "accepted_pet": false,
    "cleaning_price": 70,
    "activation": "2006-02-15",
  }
  ```
  <br /><br />
  -Select the update method and make the request<br />
  ![alt text](./req_and_res_images/route_immobles/http.png)<br />
  -A immoble can be edited by the route that receives its 'id':
  ![alt text](./req_and_res_images/route_immobles/idimmoble.png)<br />
  ![alt text](./req_and_res_images/route_immobles/responseidimmoble.png)<br />

 `/`:<br />
  - `http://127.0.0.1:8000/api/`<br />
  -This route .<br /><br />
  ![alt text](./req_and_res_images/)<br />
  ![alt text](./req_and_res_images/)<br />


 `/`:<br />
  - `http://127.0.0.1:8000/api/`<br />
  -This route .<br /><br />
  ![alt text](./req_and_res_images/)<br />
  ![alt text](./req_and_res_images/)<br />
