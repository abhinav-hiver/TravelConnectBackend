from starlette.testclient import TestClient

from src import app

client = TestClient(app)


def add_one(x):
    return x + 1


def sub_one(x):
    return x - 1


def test_answer():
    assert add_one(3) == 4
    assert sub_one(3) == 2
