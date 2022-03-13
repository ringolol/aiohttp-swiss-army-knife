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
openapi-generator-cli generate -g python-aiohttp -i docs/api/api.yaml  -o generated
```

### App factory for gunicorn
```python
import os
import connexion

async def app_factory():
    options = {
        "swagger_ui": True
        }
    specification_dir = os.path.join(os.path.dirname(__file__), 'openapi')
    app = connexion.AioHttpApp(__name__, specification_dir=specification_dir, options=options)
    app.add_api('openapi.yaml',
                arguments={'title': 'Sample API'},
                pythonic_params=True,
                pass_context_arg_name='request')

    return app.app
```
