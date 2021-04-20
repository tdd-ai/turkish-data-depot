# Turkish Data Depository Backend Application

## Django app installation and running

## Set-Up 

```shell
$ cp config/vars.env config/.env
$ nano config/.env # you need to set some env variables here 
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install req/dev.txt
$ cd tdd

$ export $(grep -v '^#' config/.env | xargs)
$ python manage.py migrate
(venv)$ python manage.py admin_setup # this will create super user using the credentials in .env file
$ python manage.py shell < dbseeder.py
$ python manage.py runserver
```

## Starting Server

$ python manage.py runserver 7000

---------

## Models

### `Dataset`

