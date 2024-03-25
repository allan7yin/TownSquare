### Prerequisites

Docker installed and running on your system. You can find installation instructions on the Docker website: https://docs.docker.com/engine/install/

1. Run the PostgreSQL Containers:
   First time, to create

```
docker run --name rewards-ecosystem-db-dev -d -p 5432:5432 -e POSTGRES_USER=dev -e POSTGRES_PASSWORD=password postgres
```

To run existing ones:

```
docker start rewards-ecosystem-db-dev
```

Check if the containers are running with

```
docker ps
```

2. Initialize Alembic to manage DB Migrations for SQLAlchemy

```
alembic init alembic
```

Set the database url

```
sqlalchemy.url = SQLALCHEMY_DATABASE_URI
```

Run migration

```
alembic revision -m "first migrations"
alembic upgrade head
```

-- This will be moved into better formated scripts later
