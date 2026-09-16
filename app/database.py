import os

import psycopg2
from psycopg2.pool import SimpleConnectionPool


DATABASE_URL = os.getenv("DATABASE_URL", "")

_pool = None


def get_pool():
    global _pool

    if _pool is None:
        if not DATABASE_URL:
            raise ValueError("DATABASE_URL تنظیم نشده است.")

        _pool = SimpleConnectionPool(
            minconn=1,
            maxconn=5,
            dsn=DATABASE_URL,
        )

    return _pool


def get_connection():
    pool = get_pool()
    return pool.getconn()


def release_connection(connection):
    if connection is not None and _pool is not None:
        _pool.putconn(connection)
