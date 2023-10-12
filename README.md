# GreenBone

The security of your IT infrastructure is important to us.

- Documentation: [Swagger Docs](http://127.0.0.1:8000/docs/) or [Re-Doc](http://127.0.0.1:8000/redoc/)


## Installation - Docker

The easiest way to get up and running is with [Docker](https://www.docker.com/).

Just [install Docker](https://www.docker.com/get-started) and
[Docker Compose](https://docs.docker.com/compose/install/)
and then run:

```
make start
```

This will spin up a PostgreSQL database, Web backend, Celery worker, and Redis broker, Notification worker, and also run your migrations.

You can then go to [localhost:8000](http://localhost:8000/) to view the app.

*Note: if you get an error, make sure you have a `.env` file, or create one based on `.env.example`.*

### Using the Makefile

You can run `make` to see other helper functions, and you can view the source
of the file in case you need to run any specific commands.

For example, you can run management commands in containers using the same method 
used in the `Makefile`. E.g.

```
docker compose exec web python manage.py createsuperuser
```

## Installation - Native

You can also install/run the app directly on your OS using the instructions below.

Setup a virtual environment and install requirements
(this example uses [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html)):

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/local.txt
```

## Set up database

*If you are using Docker you can skip these steps.*

Create a database named `gb_demo_db`.

```
createdb gb_demo_db
```

Create database migrations:

```
./manage.py makemigrations
```

Create database tables:

```
./manage.py migrate
```

## Running server

**Docker:**

```bash
make start
```

**Native:**

```bash
./manage.py runserver
```

## Running Celery

Celery can be used to run background tasks.
If you use Docker it will start automatically.

You can run it using:

```bash
celery -A gb_demo.celery_app worker -l INFO
```

Or with celery beat (for scheduled tasks):

```bash
celery -A gb_demo.celery_app worker -l INFO -B
```

## Installing Git commit hooks

To install the Git commit hooks run the following:

```shell
$ pre-commit install --install-hooks
```

Once these are installed they will be run on every commit.

## Running Tests

To run tests:

**Docker:**

```bash
make test
```

**Native:**
```bash
python manage.py test
```

## NOTES ON IMPLEMENTATION
**Module Implementation:**
- Mac address and Ip Addresses can be made unique and further validations implemented.
- Signals can also be properly tested to make sure all conditions are met.
- 

