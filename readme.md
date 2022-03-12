# AIOHTTP-SUIT

## Run
```bash
sudo docker-compose up --build --force-recreate --scale celery=2
```

## Clean-up
```bash
sudo docker-compose down -v
```

## Full clean-up
```bash
sudo docker-compose down -v --rmi 'all'
```
