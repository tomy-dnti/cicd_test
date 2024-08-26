from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/fizzbuzz/{number}")
async def fizzbuzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        return {"result": "FizzBuzz"}
    elif number % 3 == 0:
        return {"result": "Fizz"}
    elif number % 5 == 0:
        return {"result": "Buzz"}
    else:
        return {"result": str(number)}

@app.get("/factorial/{number}")
async def factorial(number: int):
    if number < 0:
        return {"error": "Negative numbers do not have factorials"}
    result = 1
    for i in range(1, number + 1):
        result *= i
    return {"result": result}