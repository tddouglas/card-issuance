# Server

These are the instructions to set up our server-sided libraries.

## Prerequisites
- [Python >= 3.9.9](https://code.visualstudio.com/docs/python/python-tutorial)
- VS Code
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Virtual environment

It is customary for pythonians to install project dependencies in virtual enviroments (advised, but not mandatory). 

Initiate a virtual environment:
```sh
python3 -m venv /path/to/virtual/environment
```

Activate virtual environment:
```sh
source path/to/venv/bin/activate
```

Deactivate virtual environment:
```sh
deactivate
```

## Install dependencies

```sh
pip3 install -r server/requirements.txt
```

## Nice to have for coding experience

### Linting
I use [flake8](https://code.visualstudio.com/docs/python/linting#_choose-a-linter).
You can install a linter in the Extensions bar of VS Code.

### Code formatter
I use [black](https://pypi.org/project/black/)

```sh
black source/file/or/directory
```
### Run the server
More details are in the [docs](https://fastapi.tiangolo.com/tutorial/first-steps/)
```sh
cd server
uvicorn app:app --reload
```

## Populate approve usecases
Sometimes, you may need to drop all tables after making schema changes. You can populate the approved usecases with the below query:
```sql
insert into approved_usecases
    (issuing_country, event_type, allowed_countries, allowed_mccs,
     max_daily_spend, max_amount_per_transaction, currency,
     payment_instrument_group_id)
values ('US', 'Recruiting', 'US', 'All MCCs', '5000', '1000', 'USD', 'PG32272223222L5JJL6WVFB3N');
insert into approved_usecases
    (issuing_country, event_type, allowed_countries, allowed_mccs,
     max_daily_spend, max_amount_per_transaction, currency,
     payment_instrument_group_id)
values ('NL', 'Internal', 'UK & EU', 'All MCCs', '5000', '1000', 'EUR', 'PG32272223222L5JJPTCWFXPP');
```
