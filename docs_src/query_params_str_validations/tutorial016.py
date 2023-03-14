from typing import List, Mapping

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Mapping[str, List[str]] = Query(default={})):
    query_items = q
    return query_items
