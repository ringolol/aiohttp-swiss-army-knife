#!/usr/bin/env python

import os
import time

import yoyo

if __name__ == "__main__":
    delay = 5
    while True:
        try:
            print("applying migration")
            user = os.environ["POSTGRES_USER"]
            password = os.environ["POSTGRES_PASSWORD"]
            db_name = os.environ["POSTGRES_DB"]
            db_address = os.environ["POSTGRES_ADDRESS"]
            backend = yoyo.get_backend(
                f"postgres://{user}:{password}@{db_address}/{db_name}"
            )
            migrations = yoyo.read_migrations("./migrations")
            backend.apply_migrations(backend.to_apply(migrations))
            print("migrations applied")
            break
        except Exception as exc:
            print(f"error applying migrations, retrying after {delay} sec \n{exc}")
        time.sleep(delay)
        delay = 2 * delay if delay < 120 else 120
