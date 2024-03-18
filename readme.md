# Room.io Take-Home with Docker Compose

This Django project uses Docker Compose to containerize the application, making it easier to set up and run across different environments.

## Prerequisites

- Docker
- Docker Compose

## Setup

**Start the Docker Containers**:

To build and start the Docker containers for the Django application, database, etc., use the following command:

```bash
docker-compose up --build
```

## Access the Application

- Once the containers are up and running, you can access the application [here](http://127.0.0.1:8000/)

## Access the Admin
```bash
username: admin
password: admin
```
- you can access the admin [here](http://127.0.0.1:8000/admin/)