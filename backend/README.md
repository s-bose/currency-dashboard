# Currency exchange backend
Written in `FastAPI`

---

## Starting the server

**Development**
```bash
uvicorn app:app --reload
```

**Production**
```bash
uvicorn app:app --host 0.0.0.0
```

---

## Testing the server
We're using [`pytest`](https://docs.pytest.org/en/7.0.x/) for testing the API. Run the tests using the following

```bash
pytest -v
```

---

## Endpoints
|`Endpoint`|`Method`|`Description`|
|:---------|:-------|:------------|
