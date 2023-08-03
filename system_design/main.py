from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND
import string
import random
from pydantic import BaseModel
import redis
import os

app = FastAPI()
redis_url = os.getenv('REDIS_URL')
r = redis.from_url(redis_url)
base_url = os.getenv('BASE_URL')

class Url(BaseModel):
    url: str

def shorten_url() -> str:
    characters = string.ascii_letters + string.digits
    while True:
        result_str = ''.join(random.choice(characters) for _ in range(9)) 
        if not r.get(result_str): 
            return result_str

@app.post("/newurl")
async def create_url(url: Url):
    existing_short_url = r.get(url.url)
    if existing_short_url:
        return {"url": url.url, "shortenUri": f"{base_url}/{existing_short_url.decode()}"}
    else:
        short_url = shorten_url()
        r.set(short_url, url.url)
        r.set(url.url, short_url)
        return {"url": url.url, "shortenUri": f"{base_url}/{short_url}"}

@app.get("/{shortened_url}")
async def redirect_url(shortened_url: str):
    url = r.get(shortened_url)
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    else:
        return RedirectResponse(url=url.decode(), status_code=HTTP_302_FOUND)