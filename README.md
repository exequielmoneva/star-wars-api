# Star Wars API

A simple API to check information about your favourite StarWars characters.
## Features:
  - get to know specfic information about the characters
  - rate them with values from 1 to 5
  - check their average rating and their top score among the community

# Stack of the project:
 - Django 3.1.2
 - Django Rest Framework 3.12.1
 - SQLite

# Requirements
 - Docker
 - Python 3.8

# Installation
Inside the root folder of the project, run the following command

```sh
> docker-compose build
```

Then start the project with the following command

```sh
> docker-compose up
```

Now, you can test the endpoints at:

```
http://localhost:8000/
```
# Available API endponits:

## GET information about a character
```
http://localhost:8000/character/character_id
```
Example response with character_id 1:
```json
{
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": {
        "name": "Tatooine",
        "population": "200000",
        "known_residents_count": 10
    },
    "species_name": null,
    "average_rating": 3.0,
    "max_rating": 5
}
```

## POST a rating for a character
```
http://localhost:8000/character/character_id/rating
```
Example body of the post:
```json
{
    "rating": 1
}
```
Example response with character_id 1:
```json
{
    "rating": 1.0,
    "character_id": 1
}
```

### ToDos

 - Write unit and integration tests
 - cache for the GET endpoints
