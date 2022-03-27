import os

import asyncpg
import connexion


async def app_factory():
    options = {"swagger_ui": True}
    specification_dir = os.path.join(os.path.dirname(__file__), "openapi")
    app = connexion.AioHttpApp(
        __name__, specification_dir=specification_dir, options=options
    )
    app.add_api(
        "openapi.yaml",
        arguments={"title": "Sample API"},
        pythonic_params=True,
        pass_context_arg_name="request",
    )

    app.app["pool"] = await asyncpg.create_pool(
        database=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_ADDRESS"],
    )

    return app.app
