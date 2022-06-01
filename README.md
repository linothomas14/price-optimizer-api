# Price Optimizer API 

This API is intended for the purposes of our capstone project at Bangkit Academy 2022 to solve the study case provided by Traveloka Singapore Company

## Table of Contents

* [Setup](#setup)
* [Routes](#routes)
* [API Documentation](#api-documentation)
* [Contributor](#contributor)

## Setup

To run this project, follow these steps:

- run `pip install -r requirements.txt` to install dependencies
- run `cp .flaskenv-example .flaskenv`
- setup .flaskenv to handle connection with database
- run `flask db init && flask db migrate && flask db upgrade`
- run `flask db_seed` to add initial user with role admin
- run `flask run`

## Routes

*Still work on progress*
| HTTP METHOD | POST            | GET       | PUT         | DELETE |
| ----------- | :-------: | :------:  | :------:  | :------: |
| /users       | - | List Users | - | - |
| /products  | Add product | List Products | - | - |
| /products`<int:id>`  | - | Detail Product | Update Product | Delete Product |


## API Documentation 

The RESTful API
* [User](#user)
    * [GET /users](#get-users)
* [Product](#product)
    * [GET /products](#get-products)
    * [POST /products](#post-products)
    * [GET /products`<int:id>`](#get-productsintid)
    * [PUT /products`<int:id>`](#put-productsintid)
* [Campaign](#campaign)
* [Promo](#promo)
* [Campaign](#campaign)
* [Promo](#promo)


## User

### GET /users
Response body  :

`status code 200 (OK)`

```json 
{
"message": "",
    "values": [
        {
            "id": 1,
            "name": "admin"
        }
    ]
}
```


## Product

### GET /products

Response body:

`status code : 200 (OK)`
```json
{
    "message": "",
    "values": [
        {
            "id": 1,
            "name": "admin"
        }
    ]
}
```
### POST /products

Response body:

`status code : 201 (CREATED)`
```
{
    "message": "Product added",
    "values": ""
}
``` 


### GET /products`<int:id>`

Response body:

`status code : 200 (OK)`
```json
{
    "message": "",
    "values": {
        "base_price": 140000,
        "competitor_price": 140000,
        "created_at": "Tue, 31 May 2022 19:06:42 GMT",
        "id": 1,
        "name": "jaket erigo",
        "product_category": "pakaian",
        "updated_at": "Tue, 31 May 2022 21:10:37 GMT"
    }
}
```

### PUT /products`<int:id>`

Response body:

`status code : 201 (CREATED)`

```
{
    "message": "update success",
    "values": ""
}
```

### Status Code
returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |

<br>

## Contributor

1. Diva Ratna Kumala Ardellia (C2006F0502)
2. Sarah Uli Octavia          (C7006F0503)
3. Yulyano Thomas Djaya       (C20090F998)


