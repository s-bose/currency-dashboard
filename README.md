hello world

FRONTEND - VueJS 3
BACKEND - FastAPI 

APIs

/currencies - GET
/convert/?from=A&?to=B - GET/ POST
/forecast/today
/forecast/tomorrow
/forecast/next/days/7
/forecast/next/days/30
/forecast               - POST datetime
/forecast               - POST from- time, to- time
/exchange_rate/currency - GET/ POST (amount)


## Portfolio
* /portfolio - GET

* /portfolio - POST
    - currency
    - amount

* /portfolio - PUT
    - id
    - new_currency
    - amount

* /portfolio - DELETE 
    - id

## Rates
- /rates - POST
    - to_currency
        - returns historical conversion graph for `to_currency` from all currencies in portfolio

- /rates/through - POST
    - from_currency
    - to_currency
    - amount
        - returns conversion rate (amount) from `from_currency` to `to_currency`
        using all available currencies as intermediates.

- 