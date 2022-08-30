# Full Stack Casting Agency API Backend

## Casting Agency Specifications

- The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Specifications

- Models:
   - Movies with attributes title, release date and genre
   - Actors with attributes name, age and gender

- Endpoints:
   - GET `/`
   - GET `/movies`
   - GET `/movies/<movie_id>`
   - POST `/movies`
   - PATCH `/moviess/<movie_id>`
   - DELETE `/moviess/<movie_id>`
   - GET `/actors`
   - GET `/actors/<actor_id>`
   - POST `/actors`
   - PATCH `/actors/<actor_id>`
   - DELETE `/actors/<actor_id>`
   
- Roles:
   -Casting Assistant
      - Can view actors and movies
   -Casting Director
      - All permissions a Casting Assistant has and
      - Add or delete an actor from the database
      - Modify actors or movies
   -Executive Producer
      - All permissions a Casting Director has and 
      - Add or delete a movie from the database

- Tests:
      - One test for success behavior of each endpoint
      - One test for error behavior of each endpoint
      - At least two tests of RBAC for each role


## Getting Started

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Create and activate the virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by running:
```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the capstone.psql file provided. From the backend folder in terminal run:

```bash
psql capstone < capstone.psql

psql capstone_testing < capstone.psql
```

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
. ./setup.sh
flask run
```

## Testing

To run the tests, run

```bash
. ./setup.sh
python test_app.py
```
## Running on heroku app:

https://castingagency101.herokuapp.com/

## Running Locally

http://127.0.0.1:5000/


setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

###### To test live APIs the only way right now to do this is curl requests and add Auth token headers from logins below to test or import the `C:\Users\Dell\OneDrive\Desktop\Udacity Projects\Capstone Casting agency\udacity-fsnd-capstone.postman_collection.json` and run in the postman.

https://ananyaudacity.us.auth0.com/authorize?audience=http://127.0.0.1:5000&response_type=token&client_id=vrXDI6tSBsQ5XUnrAUTczbyWYMlcVcjV&redirect_uri=http://localhost:8100/tabs/user-page


#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login the above link using the crededntials below and replace them in setup.sh and run setup.sh again

Casting Assistant token:
   castingassistant@gmail.com       Password: Qwerty.321
   `"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVXdklYTHVuUFFwbEFQWEI0ZDhtTyJ9.eyJpc3MiOiJodHRwczovL2FuYW55YXVkYWNpdHkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMDc3NDMzMWNkMjE2ZWZmMzBhOThiMyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTY2MTg5MjMxMywiZXhwIjoxNjYxOTc4NzEzLCJhenAiOiJ2clhESTZ0U0JzUTVYVW5yQVVUY3pieVdZTWxjVmNqViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yX2RldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllX2RldGFpbHMiLCJnZXQ6bW92aWVzIl19.IELMcYzQZ7QXz2KgqkN1R9Ti4F-aCf_1ef5RTv1dyqgo3FxZeCr3N9j3XwKDH-09KSDQ_OgtDTweREGPgNv52nIfTBp-M6C14d0fIWzVgq8uFz59tvvGao2wWvW4-XuPDp6n-Abi7lBmoowO-geUqlg8blvFexvRO-pBPNiHkuWeWxDiGudb-WXaTte8DwRAW3XQttt8cdml3aJJcka4VWFAs_2GR7N2lMqif6TnqYakaizXvRLVPsIvIq1DM9qm4sbAMjHVf9wi98fHF6_wdwZV4DzrraWc1x_BmlVrE3cNQxo4c-Pv_SjTKPewazLiqFrIlr-uekAzXNg91up_cQ"`
Casting Director token:
   castingdirector@gmail.com     Password: Qwerty.321
   `"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVXdklYTHVuUFFwbEFQWEI0ZDhtTyJ9.eyJpc3MiOiJodHRwczovL2FuYW55YXVkYWNpdHkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMDc3NGIwMzQzOGVhNDhjYjdkOWM5YyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTY2MTg5MzIxNiwiZXhwIjoxNjYxOTc5NjE2LCJhenAiOiJ2clhESTZ0U0JzUTVYVW5yQVVUY3pieVdZTWxjVmNqViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yX2RldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllX2RldGFpbHMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIl19.QjyvYQN6eWE72sYEzb00ciKf4_5udgkGTeGdRoyWu4-Q3sj-EwYq2NcPa3g4naWbZ8JgTvXzACkx4mTo5fjGVAFxBCs0cEjE2DxmY-EwjcbsFXsAuyuQ_H4ZdCZ-rR3lXl_SylPqjiWQzA4GJGBmBDLrTtK2s2JQgwYcPRkj2Y287z5UKsYQY10__CBNs-Z9CbX3rUdujT5RpPWKj_OalypGdontJQEoAuOzdrlrRq5yzq_k6SpPU_p_vm9SG3_qZF4dktSTGijm1SVl5LpufaLPQudtA-bX641amq8NmP7zXke1MONyKN8SDHvxQreF88owTFP4UtIPqBN9PTG8Zw"`
Executive Producer:
   executiveproducer@gmail.com      Password:Qwerty.321
   `"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVXdklYTHVuUFFwbEFQWEI0ZDhtTyJ9.eyJpc3MiOiJodHRwczovL2FuYW55YXVkYWNpdHkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYyZjVhNjZkN2E5MzQ5YmY1YzdiODJhNCIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTY2MTg5MzE0OSwiZXhwIjoxNjYxOTc5NTQ5LCJhenAiOiJ2clhESTZ0U0JzUTVYVW5yQVVUY3pieVdZTWxjVmNqViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yX2RldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllX2RldGFpbHMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Z--8t6uT77phG64nqzapnKv1YzGZ7ucBP_omy1Jm337TkRvwQ19iwlZoVIpt7azisEkkeKxP5Be1EzP8j4GN3ZuqmUEBy-fI-Cat3dymi82QH6Vf7xQRPJHwyZ67FXemY_EElfKI0UIS7YrGMRlRbHqXLUEEaHSh2w3OacKJapCdGv7RDXSfmazDWXcGw1iDdks8iLJjteYrBrwzJxOzK4gzNUjDoLeS6k4OnTSYvfld9my04mDB745SXWetQtApZohBuXUL0wN2JxMDu9urNdA_djSkjtBnkQY2iYbTY7AiLUJ91JoVUwFbo7Bz9ttAbLyKC7pGZVN9xUq3BdHwLg"`

#### The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{   
    "error": 400,
    "message": "bad request",
    "success": False
}

```

### API Endpoints

`GET '/'`

   - Link: `http://127.0.0.1:5000`
   - Permission: All roles
   - Returns:
      ```json
      {
         "message": "Hi, there! This is just a sample route. It means your app is working! Yippeeee!!",
         "success": true
      }
      ```


`GET '/movies'`

   - Link: `http://127.0.0.1:5000/movies`
   - Permissions: All roles
   - Returns:
      ```json
      {
         "movies": [
            {
                  "genre": "Comedy",
                  "id": 2,
                  "release_date": "2020-01-01",
                  "title": "Rush Hour"
            },
            {
                  "genre": "Romantic",
                  "id": 3,
                  "release_date": "2019-04-19",
                  "title": "After"
            },
            {
                  "genre": "Action",
                  "id": 4,
                  "release_date": "2022-07-22",
                  "title": "The Gray Man"
            },
            {
                  "genre": "Horror",
                  "id": 5,
                  "release_date": "2018-09-07",
                  "title": "The Nun"
            },
            {
                  "genre": "Sci-Fi",
                  "id": 6,
                  "release_date": "2022-06-22",
                  "title": "Spiderhead"
            },
            {
                  "genre": "SuperHero",
                  "id": 1,
                  "release_date": "2012-04-27",
                  "title": "Avengers"
            }
         ],
         "success": true
      }
      ```


`GET '/movies/<movie_id>'`

   - Link: `http://127.0.0.1:5000/movies/1`
   - Permissions: All roles
   - Returns:
      ```json
      {
         "movie": {
            "genre": "SuperHero",
            "id": 1,
            "release_date": "2012-04-27",
            "title": "Avengers"
         },
         "success": true
      }
      ```

`POST '/movies'`
   - Link: `http://127.0.0.1:5000/movies`
   - Json body: 
      ```json
         {
            "title": "Twilight",
            "release_date": "2009-11-20",
            "genre": "Romantic"
         }
      ```
   - Permissions: Only Executive Producer
   - Returns:
      ```json
      {
         "movie_id": 16, 
         "success": true
      }
      ```


`PATCH '/movies/<movie_id>'`
   - Link: `http://127.0.0.1:5000/movies/15`
   - Json body: 
      ```json
      {
         "title": "The Twilight Saga"
      }
      ```
   - Permissions: Only Casting Director and Executive Producer
   - Returns:
      ```json
      {
         "movie": {
            "genre": "Romantic",
            "id": 16,
            "release_date": "2009-11-20",
            "title": "The Twilight Saga"
         },
         "success": true
      }
      ```


`DELETE '/movies/<int:movie_id>'`
   - Link: `http://127.0.0.1:5000/movies/16`
   - Permissions: Only Executive Producer
   - Returns:
      ```json
      {
         "deleted": 16, 
         "success": true
      }
      ```


`GET '/actors'`

   - Link: `http://127.0.0.1:5000/actors`
   - Permissions: All roles
   - Returns:
      ```json
      {
         "actors": [
            {
                  "age": 41,
                  "gender": "M",
                  "id": 1,
                  "name": "Chris Evans"
            },
            {
                  "age": 68,
                  "gender": "M",
                  "id": 2,
                  "name": "Jackie Chan"
            },
            {
                  "age": 39,
                  "gender": "M",
                  "id": 3,
                  "name": "Dhanush"
            },
            {
                  "age": 28,
                  "gender": "F",
                  "id": 4,
                  "name": "Taissa Farmiga"
            },
            {
                  "age": 24,
                  "gender": "M",
                  "id": 5,
                  "name": "Hero Fiennes Tiffin"
            },
            {
                  "age": 25,
                  "gender": "F",
                  "id": 6,
                  "name": "Josephine Landford"
            },
            {
                  "age": 37,
                  "gender": "F",
                  "id": 7,
                  "name": "Scarlett Johansson"
            },
            {
                  "age": 33,
                  "gender": "F",
                  "id": 8,
                  "name": "Elizabeth Olsen"
            },
            {
                  "age": 39,
                  "gender": "M",
                  "id": 9,
                  "name": "Chris Hemsworth"
            },
            {
                  "age": 40,
                  "gender": "F",
                  "id": 31,
                  "name": "Priyanka Chopra Jonas"
            }
         ],
         "success": true
      }
      ```


`GET '/actors/<actor_id>'`

   - Link: `http://127.0.0.1:5000/actors/1`
   - Permissions: All roles
   - Returns:
      ```json
      {
         "actor": {
            "age": 41,
            "gender": "M",
            "id": 1,
            "name": "Chris Evans"
         },
         "success": true
      }
      ```


`POST '/actors'`
   - Link: `http://127.0.0.1:5000/actors`
   - Json body: 
      ```json
      {
         "name":"Alia Bhatt",
         "age": 29,
         "gender": "Female"
      }
      ```
   - Permissions: Only Casting Director and Executive Producer
   - Returns:
      ```json
      {
         "actor_id": 35, 
         "success": true
      }
      ```


`PATCH '/actors/<actor_id>'`
   - Link: `http://127.0.0.1:5000/actors/35`
   - Json body: 
      ```json
      {
         "name": "Alia Bhatt Kapoor"
      }
      ```
   - Permissions: Only Casting Director and Executive Producer
   - Returns:
      ```json
      {
         "movie": {
            "id": 35,
            "name": "Alia Bhatt Kapoor",
            "age": 29,
            "gender": "Female"
         },
         "success": true
      }
      ```


`DELETE '/movies/<int:movie_id>'`
   - Link: `http://127.0.0.1:5000/movies/35`
   - Permissions: Only Casting Director and Executive Producer
   - Returns:
      ```json
      {
         "deleted": 35, 
         "success": true
      }
      ```