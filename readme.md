# AIOHTTP-SUIT

## Docker-compose

### Run
```bash
sudo docker-compose up --build --force-recreate --scale celery=2
```

### Clean-up
```bash
sudo docker-compose down -v
```

### Full clean-up
```bash
sudo docker-compose down -v --rmi 'all'
```

##  OpenApi AIOHTTP generator

### Generate
```bash
<<<<<<< HEAD
sudo docker-compose up --build --force-recreate --scale celery=2
```

## Clean-up
```bash
sudo docker-compose down -v
```

## Full clean-up
```bash
sudo docker-compose down -v --rmi 'all'
=======
openapi-generator-cli generate -g python-aiohttp -i aiohttp/docs/api/api.yaml -o aiohttp/generated
>>>>>>> c675c48ca6a2a55fd523468a1ebde0e24f3b1e32
```
