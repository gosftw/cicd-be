from fastapi import FastAPI

app = FastAPI()

@app.get('/ping')
async def ping():
  return {'ping': 'pong'}


@app.get('/square')
async def ping(value: int):
  return {'square': value**2}