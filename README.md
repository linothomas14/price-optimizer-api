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
| /users/`<string:id>`       | - | Detail of User | - | - |
| /products  | Add product | List of Products | - | - |
| /products/`<string:id>`  | - | Detail Product | Update Product | Delete Product |
| /products?page=`<string>` | - | List of Products per Page | - | - |
| /products?category=`<string>` | - | List of Products per category | - | - |
| /products?name=`<string>` | - | List of Products that have similar name | - | - |
| /campaigns  | Add Campaign | List of Campaigns | - | - |
| /campaigns/`<int:id>`  | - | - | Update Campaign | Delete Campaign |
| /campaigns/`<int:id>`/change-active  | - | - | Change Active | - |
| /campaigns/apply-campaign  | - | - | Apply Campaign | - |
| /campaigns/predict-demand  | - | Get Predict Demand | - | - |
| /promos  | Add Promo | List of Promos | - | - |
| /promos/`<int:id>`  | - | - | Update Promo | Delete Promo |
| /vouchers  | - | List of Vouchers | - | - |
| /vouchers/`<int:id>`  | - | Get Voucher by Id | - | - |
| /template-vouchers  | - | List of Template Vouchers | - | - |
| /template-vouchers/`<int:id>`  | Add Template Voucher | - | - | Delete Template Voucher |
| /template-vouchers/`<int:id>`/predict  | predict voucher | - | - |- |


## API Documentation 
### List of Endpoints
* [User](#user)
    * [Get All Users](#get-all-users)
    * [Get User by Id](#get-user-by-id)
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
            "id": "0000366f3b9a7992bf8c76cfdf3221e2",
            "name": "Fatmir Raimonda",
            "voucher": []
        },
        {
            "id": "0000b849f77a49e4a4ce2b2a4ca5be3f",
            "name": "Ching",
            "voucher": []
        },
        {
            "id": "0000f46a3911fa3c0805444483337064",
            "name": "Haney",
            "voucher": []
        },
        {
            "id": "0000f6ccb0745a6a4b88665a16c9f078",
            "name": "Julene",
            "voucher": []
        },
        {
            "id": "0004aac84e0df4da2b147fca70cf8255",
            "name": "Dv",
            "voucher": []
        },
        {
            "id": "0004bd2a26a76fe21f786e4fbd80607f",
            "name": "Dapurkuring",
            "voucher": []
        },
        {
            "id": "00050ab1314c0e55a6ca13cf7181fecf",
            "name": "Placida",
            "voucher": []
        },
        {
            "id": "00053a61a98854899e70ed204dd4bafe",
            "name": "Teos",
            "voucher": []
        },
        {
            "id": "0005e1862207bf6ccc02e4228effd9a0",
            "name": "Sabjan",
            "voucher": []
        },
        {
            "id": "0005ef4cd20d2893f0d9fbd94d3c0d97",
            "name": "Roman",
            "voucher": []
        },
        {
            "id": "0006fdc98a402fceb4eb0ee528f6a8d4",
            "name": "Diti Bosi",
            "voucher": []
        },
        {
            "id": "00082cbe03e478190aadbea78542e933",
            "name": "Devangi",
            "voucher": []
        },
        {
            "id": "00090324bbad0e9342388303bb71ba0a",
            "name": "Vinícius",
            "voucher": []
        },
        {
            "id": "000949456b182f53c18b68d6babc79c1",
            "name": "Khashayar",
            "voucher": []
        },
        {
            "id": "000a5ad9c4601d2bbdd9ed765d5213b3",
            "name": "Pak Djie",
            "voucher": []
        },
        {
            "id": "000bfa1d2f1a41876493be685390d6d3",
            "name": "Bastoni",
            "voucher": []
        },
        {
            "id": "000c8bdb58a29e7115cfc257230fb21b",
            "name": "Lukito",
            "voucher": []
        },
        {
            "id": "000d460961d6dbfa3ec6c9f5805769e1",
            "name": "Sachini",
            "voucher": []
        },
        {
            "id": "000de6019bb59f34c099a907c151d855",
            "name": "Patrick",
            "voucher": []
        },
        {
            "id": "000e309254ab1fc5ba99dd469d36bdb4",
            "name": "Xemi",
            "voucher": []
        },
        {
            "id": "000ec5bff359e1c0ad76a81a45cb598f",
            "name": "Ardy",
            "voucher": []
        },
        {
            "id": "000ed48ceeb6f4bf8ad021a10a3c7b43",
            "name": "Muniyasamy",
            "voucher": []
        },
        {
            "id": "000fbf0473c10fc1ab6f8d2d286ce20c",
            "name": "Poerwadi",
            "voucher": []
        },
        {
            "id": "0010a452c6d13139e50b57f19f52e04e",
            "name": "Tyshaun",
            "voucher": []
        },
        {
            "id": "0010fb34b966d44409382af9e8fd5b77",
            "name": "Barman",
            "voucher": []
        },
        {
            "id": "001147e649a7b1afd577e873841632dd",
            "name": "Ayelet",
            "voucher": []
        },
        {
            "id": "00115fc7123b5310cf6d3a3aa932699e",
            "name": "Ghulam Abbas",
            "voucher": []
        },
        {
            "id": "0011805441c0d1b68b48002f1d005526",
            "name": "Mb",
            "voucher": []
        },
        {
            "id": "0011857aff0e5871ce5eb429f21cdaf5",
            "name": "Clem",
            "voucher": []
        },
        {
            "id": "0011c98589159d6149979563c504cb21",
            "name": "Magaram",
            "voucher": []
        },
        {
            "id": "0012929d977a8d7280bb277c1e5f589d",
            "name": "Prasath",
            "voucher": []
        },
        {
            "id": "0014a5a58da615f7b01a4f5e194bf5ea",
            "name": "Deep Kumar",
            "voucher": []
        },
        {
            "id": "0015752e079902b12cd00b9b7596276b",
            "name": "Ananya",
            "voucher": []
        },
        {
            "id": "00172711b30d52eea8b313a7f2cced02",
            "name": "Myo",
            "voucher": []
        },
        {
            "id": "00191a9719ef48ebb5860b130347bf33",
            "name": "Harmeet Singh",
            "voucher": []
        },
        {
            "id": "001926cef41060fae572e2e7b30bd2a4",
            "name": "Leonides",
            "voucher": []
        },
        {
            "id": "001928b561575b2821c92254a2327d06",
            "name": "Ho Ping",
            "voucher": []
        },
        {
            "id": "00196c4c9a3af7dd2ad10eade69c926f",
            "name": "Rustin",
            "voucher": []
        },
        {
            "id": "00196fdb2bf9edfc35e88ebfbcf8d781",
            "name": "Eridjol",
            "voucher": []
        },
        {
            "id": "0019da6aa6bcb27cc32f1249bd12da05",
            "name": "Liliks",
            "voucher": []
        },
        {
            "id": "0019e8c501c85848ac0966d45226fa1d",
            "name": "Djati",
            "voucher": []
        },
        {
            "id": "001a2bf0e46c684031af91fb2bce149d",
            "name": "Mehmeti",
            "voucher": []
        },
        {
            "id": "001a34eb30ecb8e3aacb07c475ca4dd1",
            "name": "Budimand",
            "voucher": []
        },
        {
            "id": "001a3a8e11d76c9a366c31a4aa2cc529",
            "name": "Afser",
            "voucher": []
        },
        {
            "id": "001ae44fa04911a9e9577356dce6c63c",
            "name": "Mo Nel",
            "voucher": []
        },
        {
            "id": "001ae5a1788703d64536c30362503e49",
            "name": "Khadeeja",
            "voucher": []
        },
        {
            "id": "001deb796b28a3a128d6113857569aa4",
            "name": "Luisada",
            "voucher": []
        },
        {
            "id": "001f3c4211216384d5fe59b041ce1461",
            "name": "Linette",
            "voucher": []
        },
        {
            "id": "002043098f10ba39a4600b6c52fbfe3c",
            "name": "Suwan",
            "voucher": []
        },
        {
            "id": "002311514717ca8b65b09a26cdf7b91a",
            "name": "Audel",
            "voucher": []
        }
    ]
}
```

### Get User by Id
* Method : GET
* URL : `/users/<string:id>`    
* Response body  :
```json 
{
    "message": "",
    "values": {
        "id": "0000366f3b9a7992bf8c76cfdf3221e2",
        "name": "Fatmir Raimonda",
        "voucher": []
    }
}
```

## Product

### Get All Products or By Page
* Method : GET
* URL : `/products`    
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
* Method : GET
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
### Get All Template Vouchers
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
* Method : POST
* URL: `/template-vouchers/<int:id>/predict`
* Response body:
```json
{
    "message": "ok,2 user have voucher",
    "values": [
        {
            "id": "c8460e4251689ba205045f3ea17884a1",
            "voucher": [
                "dfb97c88e066dc22165f31648efe1312",
                "94774f52c71a3e4ce084c21c873507cc",
                "55782cb82e0efe052da0a3da237da3b2"
            ]
        },
        {
            "id": "4546caea018ad8c692964e3382debd19",
            "voucher": [
                "dfb97c88e066dc22165f31648efe1312",
                "94774f52c71a3e4ce084c21c873507cc",
                "55782cb82e0efe052da0a3da237da3b2"
            ]
        }
    ]
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


