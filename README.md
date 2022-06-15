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
- run `cp .env-example .env`
- setup .env to handle connection with database
- run `flask db init`
- run `flask db migrate`
- run `flask db upgrade`
- run `flask run`

## Routes

| HTTP METHOD | POST            | GET       | PUT         | DELETE |
| ----------- | :-------: | :------:  | :------:  | :------: |
| /users       | - | List of Users | - | - |
| /products  | Add product | List of Products | - | - |
| /products/`<string:id>`  | - | Detail Product | Update Product | Delete Product |
| /products?page=`<string>` | - | List of Products per Page | - | - |
| /products?category=`<string>` | - | List of Products per category | - | - |
| /products?name=`<string>` | - | List of Products that have similar name | - | - |
| /campaigns  | Add Campaign | List of Campaigns | - | - |
| /campaigns/`<int:id>`  | - | - | Update Campaign | Delete Campaign |
| /promos  | Add Promo | List of Promos | - | - |
| /promos/`<int:id>`  | - | - | Update Promo | Delete Promo |
| /vouchers  | - | List of Vouchers | - | - |
| /vouchers/`<int:id>`  | - | Get Voucher by Id | - | - |
| /template-vouchers  | - | List of Template Vouchers | - | - |
| /template-vouchers/`<int:id>`  | Add Template Voucher | - | Update Template Voucher | Delete Template Voucher |


## API Documentation 
### List of Endpoints
* [User](#user)
    * [Get All Users](#get-all-users)
* [Product](#product)
    * [Get All Products or By Page](#get-all-products-or-by-page)
    * [Get Products By Category](#get-products-by-category)
    * [Get Product By Id](#get-product-by-id)
    * [Add Product](#add-product)
    * [Update Product](#update-product)
    * [Delete Product](#delete-product)
* [Campaign](#campaign)
    * [Get All Campaigns](#get-all-campaigns)
    * [Add Campaign](#add-campaign)
    * [Update Campaign](#update-campaign)
    * [Delete Campaign](#delete-campaign)
    * [Change Active](#change-active)
    * [Apply Campaign](#apply-campaign)
    * [Predict Campaign](#predict-campaign)
* [Promo](#promo)
    * [Get All Promos](#get-all-promos)
    * [Add Promo](#add-promo)
    * [Update Promo](#update-promo)
    * [Delete Promo](#delete-promo)
* [Voucher](#voucher)
    * [Get All Vouchers](#get-all-vouchers)
    * [Get Voucher by Id](#get-voucher-by-id)
* [Template Voucher](#voucher-template)
    * [Get All Template Vouchers](#get-all-template-vouchers)
    * [Add Template Voucher](#add-template-voucher)
    * [Update Template Voucher](#update-template-voucher)
    * [Delete Template Voucher](#delete-template-voucher)
    * [Predict Voucher](#predict-voucher)

## User

### Get All Users
* Method : GET
* URL : `/users`    
* Response body  :
```json 
{
    "message": "",
    "values": [
        {
            "id": "000161a058600d5901f007fab4c27140",
            "name": "",
            "voucher": []
        },
        {
            "id": "0001fd6190edaaf884bcaf3d49edf079",
            "name": "",
            "voucher": []
        },
        {
            "id": "000379cdec625522490c315e70c7a9fb",
            "name": "",
            "voucher": []
        },
        {
            "id": "0004164d20a9e969af783496f3408652",
            "name": "",
            "voucher": []
        },
        {
            "id": "000419c5494106c306a97b5635748086",
            "name": "",
            "voucher": []
        }
    ]
}
```


## Product

### Get All Products or By Page
* Method : GET
* URL : `/products` or `/products?page=<int>`    
* Response body  :
```json
{
    "message": "",
    "values": [
        {
            "base_price": 310390.0,
            "competitor_price": 349000,
            "created_at": "Sun, 20 May 2018 18:45:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00066f42aeeb9f3007548bb9d3f33c38",
            "name": "Euodia Parfums Freese 30 ml",
            "product_category": "perfumery",
            "updated_at": "Sun, 20 May 2018 18:45:00 GMT"
        },
        {
            "base_price": 396652.0,
            "competitor_price": 600000,
            "created_at": "Tue, 12 Dec 2017 19:20:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00088930e925c41fd95ebfe695fd2655",
            "name": "kaca film 3m auto film dpn 40%.black beauty.",
            "product_category": "auto",
            "updated_at": "Tue, 12 Dec 2017 19:20:00 GMT"
        },
        {
            "base_price": 699256.0,
            "competitor_price": 988900,
            "created_at": "Thu, 21 Dec 2017 16:21:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "0009406fd7479715e4bef61dd91f2462",
            "name": "Bed & Bath Leaf Medley Cutwork Table Runner  54 Inches by 54 Inches",
            "product_category": "bed_bath_table",
            "updated_at": "Thu, 21 Dec 2017 16:21:00 GMT"
        },
        {
            "base_price": 179852.0,
            "competitor_price": 1701600,
            "created_at": "Wed, 01 Aug 2018 22:00:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "000b8f95fcb9e0096488278317764d19",
            "name": "NACHTMANN SQUARE VASE 28CM SET/1",
            "product_category": "housewares",
            "updated_at": "Fri, 10 Aug 2018 13:24:00 GMT"
        },
        {
            "base_price": 607650.0,
            "competitor_price": 1430000,
            "created_at": "Tue, 03 Apr 2018 09:24:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "000d9be29b5207b54e86aa1b1ac54872",
            "name": "Jam Tangan Pria Guess W1108G4 Navy Men Watch Gift Color Original + Box",
            "product_category": "watches_gifts",
            "updated_at": "Tue, 03 Apr 2018 09:24:00 GMT"
        },
        {
            "base_price": 158783.0,
            "competitor_price": 332000,
            "created_at": "Thu, 14 Dec 2017 20:30:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "0011c512eb256aa0dbbb544d8dffcf6e",
            "name": "Paket Komplit Perawatan Mobil Premium ZERONE JAPAN Mobil Auto Bersih",
            "product_category": "auto",
            "updated_at": "Thu, 14 Dec 2017 20:30:00 GMT"
        },
        {
            "base_price": 760326.0,
            "competitor_price": 921000,
            "created_at": "Sun, 17 Sep 2017 20:35:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00126f27c813603687e6ce486d909d01",
            "name": "How to Draw Cool Stuff: A Drawing Guide for Teachers and Students",
            "product_category": "cool_stuff",
            "updated_at": "Sun, 17 Sep 2017 20:45:00 GMT"
        },
        {
            "base_price": 118782.0,
            "competitor_price": 1200000,
            "created_at": "Sat, 28 Oct 2017 18:16:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "001795ec6f1b187d37335e1c4704762e",
            "name": "Anbernic RG280V / Nintendo / Retro Game / Game Boy / Sega - Kuning",
            "product_category": "consoles_games",
            "updated_at": "Wed, 27 Dec 2017 00:22:00 GMT"
        },
        {
            "base_price": 240923.0,
            "competitor_price": 308750,
            "created_at": "Thu, 09 Aug 2018 01:24:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "001b237c0e9bb435f2e54071129237e9",
            "name": "Kitchen Cook jumbo SPATULA \"our Table\" import USA Bed Bath Beyond",
            "product_category": "bed_bath_table",
            "updated_at": "Thu, 09 Aug 2018 01:24:00 GMT"
        },
        {
            "base_price": 106843.0,
            "competitor_price": 8000000,
            "created_at": "Wed, 15 Feb 2017 23:49:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "001b72dfd63e9833e8c02742adf472e3",
            "name": "Celine Credenza / Meja Pajangan Lemari Penyimpanan Gold Emas Furniture",
            "product_category": "furniture_decor",
            "updated_at": "Fri, 15 Dec 2017 09:16:00 GMT"
        }
    ]
}
```
### Get Products By Category
* Method : GET
* URL : `/products?category=<string>`    
* Response body  :
```json
{
    "message": "",
    "values": [
        {
            "base_price": 396652.0,
            "competitor_price": 600000,
            "created_at": "Tue, 12 Dec 2017 19:20:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00088930e925c41fd95ebfe695fd2655",
            "name": "kaca film 3m auto film dpn 40%.black beauty.",
            "product_category": "auto",
            "updated_at": "Tue, 12 Dec 2017 19:20:00 GMT"
        },
        {
            "base_price": 158783.0,
            "competitor_price": 332000,
            "created_at": "Thu, 14 Dec 2017 20:30:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "0011c512eb256aa0dbbb544d8dffcf6e",
            "name": "Paket Komplit Perawatan Mobil Premium ZERONE JAPAN Mobil Auto Bersih",
            "product_category": "auto",
            "updated_at": "Thu, 14 Dec 2017 20:30:00 GMT"
        },
        {
            "base_price": 182906.0,
            "competitor_price": 209000,
            "created_at": "Sat, 19 May 2018 14:46:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "006c67546bfe73c33b83f6bd1ad58c36",
            "name": "Auto Detailing Paket 7 Varian Pengkilap Kendaraan Mobil Motor Premium",
            "product_category": "auto",
            "updated_at": "Sat, 19 May 2018 14:46:00 GMT"
        },
        {
            "base_price": 2900540.0,
            "competitor_price": 8202000,
            "created_at": "Mon, 14 May 2018 21:03:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "009df2b0bc078648fc4f5898de8cabff",
            "name": "SCAN TOOL XTOOL X100 PAD OBD2 Auto Key Programmer Diagnostic Scanner T",
            "product_category": "auto",
            "updated_at": "Mon, 14 May 2018 21:03:00 GMT"
        },
        {
            "base_price": 393935.0,
            "competitor_price": 749000,
            "created_at": "Mon, 30 Jul 2018 18:41:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00b264091d1c8df03976c3f3b176b35c",
            "name": "70mai Smart Dash Cam Wifi M300 1296P Recorder Auto Car Camera",
            "product_category": "auto",
            "updated_at": "Mon, 30 Jul 2018 18:41:00 GMT"
        },
        {
            "base_price": 821030.0,
            "competitor_price": 2100000,
            "created_at": "Mon, 27 Nov 2017 12:12:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00bb62ea3729537a687c3fddcd123662",
            "name": "Defi Advance ZD Digital Auto Meter",
            "product_category": "auto",
            "updated_at": "Mon, 27 Nov 2017 12:12:00 GMT"
        },
        {
            "base_price": 362758.0,
            "competitor_price": 617500,
            "created_at": "Tue, 31 Jul 2018 18:18:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "00de606a5dda99c2499f94ef18282977",
            "name": "CARLINKIT Wireless Dongle Carplay Android Auto Android Headunit Wired",
            "product_category": "auto",
            "updated_at": "Tue, 31 Jul 2018 18:18:00 GMT"
        },
        {
            "base_price": 182906.0,
            "competitor_price": 209000,
            "created_at": "Sun, 26 Nov 2017 07:52:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "0110986ff84d644fee920efb18577292",
            "name": "Auto Detailing Paket 7 Varian Pengkilap Kendaraan Mobil Motor Premium",
            "product_category": "auto",
            "updated_at": "Sun, 26 Nov 2017 07:52:00 GMT"
        },
        {
            "base_price": 120614.0,
            "competitor_price": 135000,
            "created_at": "Mon, 11 Dec 2017 01:05:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "0168e1b28d8e55a515928cf656eff0a4",
            "name": "Paket NYOC ONE KLIN+Auto Purifier-car fogging-car interior cleaner",
            "product_category": "auto",
            "updated_at": "Tue, 24 Jul 2018 09:09:00 GMT"
        },
        {
            "base_price": 167638.0,
            "competitor_price": 898000,
            "created_at": "Sun, 01 Oct 2017 11:21:00 GMT",
            "discount": 0.0,
            "final_price": 0.0,
            "id": "016f3b29107ed03252e477b08445cec4",
            "name": "Auto Headlight System With Follow Me Home Jazz GK5 by PlugNPlay",
            "product_category": "auto",
            "updated_at": "Sun, 01 Oct 2017 11:21:00 GMT"
        }
    ]
}
```

### Get Product By Id
* Method : GET
* URL : `/products/<string:id>`    
* Response body  :
```json
{
    "message": "",
    "values": {
        "base_price": 310390.0,
        "competitor_price": 349000,
        "created_at": "Sun, 20 May 2018 18:45:00 GMT",
        "discount": 0.0,
        "final_price": 0.0,
        "id": "00066f42aeeb9f3007548bb9d3f33c38",
        "name": "Euodia Parfums Freese 30 ml",
        "product_category": "perfumery",
        "updated_at": "Sun, 20 May 2018 18:45:00 GMT"
    }
}
```

### Add Product
* Method : POST
* URL : `/products`    
* Request body :
```json
{
    "name" : "jaket erigo",
    "base_price" : 159000,
    "product_category" : "Pakaian"
}
```
* Response body:
```json
{
    "message": "Product added",
    "values": ""
}
``` 

### Update Product
* Method : PUT
* URL : `/products/<string:id>`       
* Request body:
```json
{
    "name" : "baju",
    "base_price" : 140000
}
```
* Response body:
`status code 201`
```json
{
    "message": "successfully updated",
    "values": ""
}
```

### Delete Product
* Method : DELETE
* URL : `/products/<string:id>`    
* Response body :
```json
{
    "message": "product deleted",
    "values": ""
}
```



## Campaign
### Get All Campaigns
* Method : GET
* URL : `/campaigns`    
* Response body :
```json
{
    "message": "",
    "values": [
        {
            "created_at": "Thu, 02 Jun 2022 14:23:12 GMT",
            "end_date": "Tue, 10 May 2022 00:00:00 GMT",
            "every_weekend": false,
            "id": 1,
            "is_active": false,
            "name": "Back to School",
            "periodical": true,
            "promo": [
                {
                    "campaign_id": 1,
                    "category_name": "peralatan alat tulis",
                    "created_at": "Thu, 02 Jun 2022 14:41:33 GMT",
                    "discount": 0.1,
                    "id": 1,
                    "max_discount": 10000.0,
                    "name": "Diskon Alat Tulis",
                    "updated_at": "Thu, 02 Jun 2022 14:41:33 GMT"
                }
            ],
            "start_date": "Sun, 01 May 2022 00:00:00 GMT",
            "updated_at": "Thu, 02 Jun 2022 14:23:12 GMT"
        }
    ]
}
```

### Add Campaign
* Method : POST
* URL : `/campaigns`    
* Request body :
```json
{
    "name" : "Back to School",
    "start_date" : "2022-05-01",
    "end_date" : "2022-05-10",
    "periodical" : true,
    "every_weekend" : false

}
```
* Response body:
```json
{
    "message": "Campaign added",
    "values": ""
}
``` 

### Update Campaign
* Method : PUT
* URL: `/campaigns/<int:id>`
* Request body:
```json
{
    "name" : "Back to School 2022",
    "category_name" : "peralatan alat tulis",
    "start_date" : "2022-05-01",
    "end_date" : "2022-05-10",
    "periodical" : true,
    "every_weekend" : true,
    "is_active" : true

}
```
* Response body :
`status code 201`
```json
{
    "message": "successfully updated",
    "values": ""
}
```
`status code 400`
```json
{
    "message": "campaign not found",
    "values": ""
}
```

### Delete Campaigns
* Method : DELETE
* URL : `/campaigns<int:id>`    
* Response body :
```json
{
    "message": "campaign deleted",
    "values": ""
}
```

### Change Active
* Method : PUT
* URL: `/campaigns/<int:id>/change_active`
* Request body:
```json
{
    "is_active" : true
}
```
* Response body :
`status code 201`
```json
{
    "message": "Campaign Turned ON",
    "values": ""
}
```
### Apply Campaign
* Method : PUT
* URL: `/campaigns/apply-campaign`
* Response body :
`status code 201`
```json
{
    "message": "Successs",
    "values": ""
}
```
### Predict Campaign
* Method : PUT
* URL: `/campaigns/predict-demand`
* Response body :
`status code 201`
```json
{
    "message": "OK",
    "values": {
        "auto": [
            67,
            79,
            11,
            79,
            11,
            12,
            56,
            67,
            12,
            11,
            67,
            28,
            12,
            11
        ]
    }
}
```

## Promo
### Get All Promos
* Method : POST
* URL: `/promos`
* Response body:
```json
{
    "message": "",
    "values": [
        {
            "campaign_id": 1,
            "category_name": "peralatan alat tulis",
            "created_at": "Thu, 02 Jun 2022 14:41:33 GMT",
            "discount": 0.1,
            "id": 1,
            "max_discount": 10000.0,
            "name": "Diskon Alat Tulis",
            "updated_at": "Thu, 02 Jun 2022 14:41:33 GMT"
        }
    ]
}
```

### Add Promo
* Method : POST
* URL: `/promos`
* Request body:
```json
{
    "name": "Diskon Alat Tulis",
    "discount" : 0.1,
    "category_name": "peralatan alat tulis",
    "campaign_id" : 1,
    "max_discount": 10000
}
```
* Response body:
```json
{
    "message": "Promo added",
    "values": ""
}
```

### Update Promo
* Method : PUT
* URL: `/promos/<int:id>`
* Request body:
```json
{
    "name": "Diskon Alat Tulis",
    "category_name" : "Peralatan Alat Tulis",
    "discount" : 0.2,
    "max_discount": 5000
}
```
* Response body:
`if succeed`
```json
{
    "message": "successfully updated",
    "values": ""
}
```
`if total discount reach 100%`
```json
{
    "message": "successfully updated",
    "values": "Discount reach 100%"
}
```
`else`
```json
{
    "message": "Bad request",
    "values": "error"
}
```

### Delete Promo
* Method : DELETE
* URL : `/promos/<int:id>`    
* Response body :
```json
{
    "message": "promo deleted",
    "values": ""
}
```

## Voucher
### Get All Vouchers
* Method : GET
* URL: `/vouchers`
* Response body:
```json
{
    "message": "",
    "values": [
        {
            "id": 1,
            "max_discount": 20000.0,
            "product_id": "00066f42aeeb9f3007548bb9d3f33c38",
            "name": "Voucher parfum"
        }
    ]
}
```

### Get Voucher by Id
* Method : GET
* URL: `/vouchers/<int:id>`
* Response body:
```json
{
    "message": "",
    "values": [
        {
            "id": 1,
            "max_discount": 20000.0,
            "product_id": "00066f42aeeb9f3007548bb9d3f33c38",
            "name": "Voucher parfum"
        }
    ]
}
```
`if not found`
```json
{
    "message": "voucher not found",
    "values": []
}
```

##  Template Voucher
### Get All Tempate Vouchers
* Method : GET
* URL: `/template-vouchers`
* Response body:
```json
{
    "message": "",
    "values": [
        {
            "budget": 100000,
            "category_name": "auto",
            "created_at": "Sat, 11 Jun 2022 15:31:16 GMT",
            "experied_date": "Mon, 10 Oct 2022 00:00:00 GMT",
            "id": 1,
            "max_discount": 20000.0,
            "name": "Voucher parfum",
            "updated_at": "Sat, 11 Jun 2022 15:31:16 GMT"
        }
    ]
}
```
### Add Template Voucher
* Method : POST
* URL: `/template-vouchers`
* Request body:
```json
{
    "name": "Voucher parfum",
    "category_name": "auto",
    "max_discount": 20000,
    "budget": 100000,
    "experied_date": "2022-10-10"
}
``` 
* Response body:
```json
{
    "message": "Voucher added",
    "values": ""
}
```

### Update Template Voucher
* Method : PUT
* URL: `/template-vouchers/<int:id>`
* Request body:
```json
{
    "name": "Voucher parfum",
    "category_name": "perfumery",
    "max_discount": 0.12,
    "budget": 100000,
    "experied_date": "2022-10-10"
}
```
* Response body:
```json
{
    "message": "successfully updated",
    "values": ""
}
```

### Delete Template Voucher
* Method : DELETE
* URL: `/template-vouchers/<int:id>`
* Response body:
```json
{
    "message": "Vocuher deleted",
    "values": ""
}
```

### Predict Voucher
* Method : GET
* URL: `/template-vouchers/1/predict`
* Response body:
```json
{
    "message": "Vocuher deleted",
    "values": ""
}
```

## Status Code
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


