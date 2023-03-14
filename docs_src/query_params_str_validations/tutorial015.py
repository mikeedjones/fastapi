from typing import Mapping

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Mapping[str, str] = Query(default={})):
    query_items = q
    return query_items
