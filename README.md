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
