# Currency Dashboard

## Stack:

`VueJS` Frontend | `FastAPI` Backend

## Necessary endpoints

|**Endpoints**|**Method**|**Remarks**|
|:------------|:---------|:----------|
|`/currencies`|`GET`||
|`/convert/?from=A&?to=B`|`GET`, `POST`||
|`/forecast/today`|`GET`||
|`/forecast/tomorrow`|`GET`||
|/forecast/next/days/7|`GET`||
|/forecast/next/days/30|`GET`||
|`/forecast`|`POST`|datetime|
|`/forecast`|`POST`|from- time, to- time|
|`/exchange_rate/currency`|`GET`, `POST`|amount|


## Portfolio

|**Endpoints**|**Method**|**Remarks**|
|:------------|:---------|:----------|
|`/portfolio`|`GET`||
|`/portfolio`|`POST`| `currency`, `amount`|
|`/portfolio`| `PUT`|`id`,`new_currency`,`amount`| 
|`/portfolio`|`DELETE`|`id`|

## Rates
|**Endpoints**|**Method**|**Remarks**|
|:------------|:---------|:----------|
|`/rates`|`POST`|`to_currency`, returns historical conversion graph for `to_currency` from all currencies in portfolio|
|`/rates/through`|`POST`|`from_currency`,`to_currency`,`amount`, returns conversion rate (amount) from `from_currency` to `to_currency`
        using all available currencies as intermediates.|

## Possible choices for Sources

- https://exchangerate.host/#/
- https://freecurrencyapi.net/
- https://www.fxstreet.com/rates-charts/forecast
