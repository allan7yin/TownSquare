### Prerequisites

Docker installed and running on your system. You can find installation instructions on the Docker website: https://docs.docker.com/engine/install/

1. Run the PostgreSQL Containers

```
docker run --name rewards-ecosystem-db -d -p 5432:5432 -e POSTGRES_PASSWORD=password postgres
docker run --name gpt-marketing -d -p 5433:5432 -e POSTGRES_PASSWORD=password postgres
```

Check if the containers are running with

```
docker ps
```
