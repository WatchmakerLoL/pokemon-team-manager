# pokemon-team-manager

This project is a technical exercise provided by an employer.

## How to install the project

1. Clone the repository.

This project is available on Github. Clone with your prefered git tool or with the command:

` git clone https://github.com/WatchmakerLoL/pokemon-team-manager.git `
2. Set up a virtual environment and activate it.

Go to a folder outside the project and create the virtualenv using the following command:

` python3 -m venv /path/to/new/virtual/environment `
 
Then you should activate it by running the following command inside the virtualenv folder:

` activate `

4. Install dependencies from requirements.txt.

Go back to repo's root and run the following command:

` pip install -r requirements.txt `

This will install all necessary dependencies.

4. Set up a Postgresql database.

This project uses environment variables to configure database connection. Go to 

> pokemon_team_manager/.env

Change the variables to point to your postgresql database. In this example "pokemon_manager"

5. Run the server.

` python manage.py runserver `


## How to use the API

This API has 3 endpoints.

- trainers
- teams
- pokemons

Every endpoint has the following methods allowed:

| URL             | Method | Action         |
|-----------------|--------|----------------|
| {basename}/     | GET    | List           |
| {basename}/{id} | GET    | Retrieve       |
| {basename}/     | POST | Create         |
| {basename}/{id} | PUT | Update         |
| {basename}/{id} | PATCH | Partial Update |
| {basename}/{id} | DELETE | Destroy        |

For example, if we wanted to get a list of all pokemon trainers we would make a GET request to

> trainers/

And if we wanted to create a new trainer we would post to that same url the following data:

> { 
>  "name": "Trainer",
>  "age": "10",
>  "gender": "M"
> }

## Technical Stack.


|                       | Version |
|-----------------------|---------|
| Python                | 3.9     |
| Django                | 4.0     |
| Django Rest Framework | 3.13.1  |
