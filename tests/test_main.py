from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test_read_root():
    return {"message": "Hello, World!"}
