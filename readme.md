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
flask run
```
## Running on heroku app:

https://capstonecastingproject0044.herokuapp.com/

## Running Locally

setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

###### To test live APIs the only way right now to do this is curl requests and add Auth token headers from logins below to test or import the `C:\Users\Dell\OneDrive\Desktop\Udacity Projects\Capstone Casting agency\udacity-fsnd-capstone.postman_collection.json` and run in the postman.

https://ananyaudacity.us.auth0.com/authorize?audience=http://127.0.0.1:5000&response_type=token&client_id=vrXDI6tSBsQ5XUnrAUTczbyWYMlcVcjV&redirect_uri=http://localhost:8100/tabs/user-page


#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login the above link using the crededntials below and replace them in setup.sh and run setup.sh again

Casting Assistant token:
   castingassistant@gmail.com       Password: Qwerty.321
   `"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVXdklYTHVuUFFwbEFQWEI0ZDhtTyJ9.eyJpc3MiOiJodHRwczovL2FuYW55YXVkYWNpdHkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMDc3NDMzMWNkMjE2ZWZmMzBhOThiMyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTY2MTgwMjYwMSwiZXhwIjoxNjYxODg5MDAxLCJhenAiOiJ2clhESTZ0U0JzUTVYVW5yQVVUY3pieVdZTWxjVmNqViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yX2RldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllX2RldGFpbHMiLCJnZXQ6bW92aWVzIl19.19rY2QiM_ZHw8zDlPMAk1UTJtTJj8ERWi2ap0NMifSmkyQDqBNjwapYx2lpS4T8Ku_HZL0OK4fG3Se4dSfRw1fujdUWEpsGi4Og61khtzNMjp42uMVSb0DfOeZlR9syCaPVkXMjoIqEvV_qvCibKFe68ziyjsm45skG2w8kTRu9XTENXa8v3QXImeY5e2cZKaPuTjFxItrDbt1vdDaRhp1EzFGBxZSxoumtG-MI9TMOzJ5vfqB61U2f9f4theomvNbcrv4-GP-LKMlfSSKrbXvACl9GtIeET5Woxeg4awCopmxjk1CxXLx0ShQLh88SWCz8esGJTkH7HUNiTbTEYIA"`
Casting Director token:
   castingdirector@gmail.com     Password: Qwerty.321
   `"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVXdklYTHVuUFFwbEFQWEI0ZDhtTyJ9.eyJpc3MiOiJodHRwczovL2FuYW55YXVkYWNpdHkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMDc3NGIwMzQzOGVhNDhjYjdkOWM5YyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTY2MTgwMjY4NSwiZXhwIjoxNjYxODg5MDg1LCJhenAiOiJ2clhESTZ0U0JzUTVYVW5yQVVUY3pieVdZTWxjVmNqViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yX2RldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllX2RldGFpbHMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIl19.EQbbTOZQnBnId_hZkUIAX9g57pb_Z1GQ0hs9syJH_WQFvT8HRPy2z6kAp_RVmVq30NF4Wo8cucUKVcW5CTmllW90RILF6BhvzXfzXhYSVkAhB17hkRMalnykRu2MENUdHHG2AXV-zJKVcD8rGrFWL9NFwb5_fk_n58aEr8acQ5iNX_Mci0kEK-anQbOfSPzJ_fNJTTRzzdRdibPQRP4T4LxVCHrxMd39QV3Q6CcDwZOQu60fT3DIyIo1eNCCU-knOaKEJNznXT-i-PLg5MLyIg95zQEkcz4KWhqF1cFupcHkCosa9FgeMKMkPqC_gMROUlWhQRuH0SpLCVqt5O35Gw"`
Executive Producer:
   executiveproducer@gmail.com      Password:Qwerty.321
   `"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVXdklYTHVuUFFwbEFQWEI0ZDhtTyJ9.eyJpc3MiOiJodHRwczovL2FuYW55YXVkYWNpdHkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYyZjVhNjZkN2E5MzQ5YmY1YzdiODJhNCIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjE6NTAwMCIsImlhdCI6MTY2MTgwMjkyNCwiZXhwIjoxNjYxODg5MzI0LCJhenAiOiJ2clhESTZ0U0JzUTVYVW5yQVVUY3pieVdZTWxjVmNqViIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yX2RldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllX2RldGFpbHMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.aJpZjHentJ9NbF9fooBIMrlPifzy75rAv1lCT7Lzn3kcm27uibULZxpdZ_fT0Nv0o0V8V0UHfkO6pVCnM-e7AUSmDxwxZKUOgY9o9w0rvlqY4Ub3BSvJog_sQXJ0HpWDeMxw_8WFhMRAowuvxuIidcw-0-6WhMUmV3gf0jcQY9_F_Mf29J9WtdlkNEYnszmz7llnragFiNiNiwixNk3fqHkxskPxn93aDTNRjEu6K6W6QGYmYjdJ0TnunFPSLVaghslUhiwdeaDqDGj3kYiCoSqJeyuybpqss-VEJKkJkHMATLBt_lcpntPYx60zY_ob4CWqAQB1GIBo4etFMbUP8w"`

## Project deployed at

https://castingagency101.herokuapp.com/

## Project locally deployed at

http://127.0.0.1:5000/

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