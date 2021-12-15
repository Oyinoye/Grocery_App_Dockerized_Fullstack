# Full Stack Grocery App 

The source code for Rideco Grocery App project.
Was run in ubuntu dev invironment.

## Dockerized in Django with Postgres, Gunicorn, and Nginx

Three separate containers to run the three services:
- Container for Django backend
- Container for React frontend
- Container for PostgreSQL database

## Setup

Setup using docker using docker commands.

Includes develpment setup and production setup with respective environment variables.

My environment variables file (.env.dev) looks something like:

DEBUG=1
SECRET_KEY=verysecret
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=grocery_app_dev
SQL_USER=grocery_app
SQL_PASSWORD=grocery_app
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

### Other info

Uses the default Django development server.

1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
