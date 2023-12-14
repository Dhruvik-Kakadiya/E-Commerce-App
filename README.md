
# E-Commerce APp

This is a backend django project for E-Commerce service


## Prerequisites

- [Python](https://www.python.org/downloads/) v3.10.0+
- [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-pip) v21.0.0+
- [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)

## Setup Django Project

Clone the project

_using ssh_

```bash
```

_or using https_

```bash
```

Go to the project directory

```bash
cd ecommerce_app
```

Create a virtual environment

```bash
python3 -m venv ./venv
```

Activate a virtual environment

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

### <span id="generate_secret_key">Create a new secret key for your project</span>

For that, open up django shell using

```bash
python manage.py shell
```

Then write these commands

```py
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

Copy output of `get_random_secret_key()`, without quotes, that's your secret key.
Update your environment file with this secret key

Close django shell

```py
exit()
```

## Run using runserver

Run the migrations first

```bash
python manage.py migrate
```

To run the python server

```bash
python manage.py runserver
```

To create your admin user

```bash
python manage.py createsuperuser
```