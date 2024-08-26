import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_fizzbuzz():
    response = client.get("/fizzbuzz/15")
    assert response.status_code == 200
    assert response.json() == {"result": "FizzBuzz"}

    response = client.get("/fizzbuzz/3")
    assert response.status_code == 200
    assert response.json() == {"result": "Fizz"}

    response = client.get("/fizzbuzz/5")
    assert response.status_code == 200
    assert response.json() == {"result": "Buzz"}

    response = client.get("/fizzbuzz/7")
    assert response.status_code == 200
    assert response.json() == {"result": "7"}

def test_factorial():
    response = client.get("/factorial/5")
    assert response.status_code == 200
    assert response.json() == {"result": 120}

    response = client.get("/factorial/0")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    response = client.get("/factorial/-1")
    assert response.status_code == 200
    assert response.json() == {"error": "Negative numbers do not have factorials"}