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
uvicorn main:app --reload
```
