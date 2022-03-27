"""
create test table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE SCHEMA IF NOT EXISTS test;"),
    step("CREATE TABLE IF NOT EXISTS test.table (id serial, data text);"),
]
