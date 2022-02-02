# Serverless Functions

[serverless](https://www.ibm.com/cloud/learn/serverless)

- Provisions resources on demand
- Automatically scalable
- Automatically scales to 0 when not in use

Cloud services free up infrastructure and equipment constraints. Services not used are also cheaper to maintain since billing is related to use.\
Monitoring and debugging across large infrastructure can be difficult.

## FaaS Function as a service

- Application code runs in containers upon request.

## Kubernetes and Knative

Open source container orchestration platforms.

## Python Environments

with no mention of path

[Python Environments](https://realpython.com/effective-python-environment/)

### pyenv

```terminal
pyenv versions
pyenv install 3.7.3
pyenv versions

pyenv global 3.9.5
pyenv local 3.8
pyenv shell 3.9

```

### venv

create environments by passing a path

```terminal
python -m venv ~/.virtualenvs/my-env

# activate the path
source ~/.virtualenvs/my-env/bin/activate

$ deactivate

```

### pyenv-virtualenv

an enhanced version of pyenv

```terminal
$ pyenv virtualenv 3.7.3 my-env

$ pyenv activate my-env

$ pyenv deactivate

```

### pipenv

> includes package management

```terminal
pipenv install

pipenv install numpy

pipenv shell


exit
```

### Poetry

> includes package management

```terminal
poetry new <project>

poetry install

poetry shell

```


[http.server](https://pymotw.com/3/http.server/index.html)

```python
from http.server import BaseHTTPRequestHandler
from urllib import parse
```

A base http handler class. Methods take no arguments and the request is available within the parsed request.



[Request HTTP for Humans](https://docs.python-requests.org/en/latest/)

Http handling library.


### SOAP vs REST

- SOAP: Simple Object Access Protocol. Strict contract based usage. Designed around actions.
- REST: Representational State Transfer. Public data fetching. Lighter an easier to align with HTTP.
- GraphQL: A customizable typed api query language.

```python
import requests
response = requests.get('http://something_something.com/api/garbage')
response.text
```
