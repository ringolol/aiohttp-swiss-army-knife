# AIOHTTP-SUIT

## Docker-compose

### Run
```bash
sudo docker-compose up --build --force-recreate --scale dramatiq=2
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
openapi-generator-cli generate -g python-aiohttp -i aiohttp/docs/api/api.yaml -o aiohttp/generated
```
