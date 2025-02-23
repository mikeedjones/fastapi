from typing import Dict, List, Tuple

import pytest
from fastapi import FastAPI, Query
from pydantic import BaseModel


def test_invalid_sequence():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: List[Item] = Query(default=None)):
            pass  # pragma: no cover


def test_invalid_tuple():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Tuple[Item, Item] = Query(default=None)):
            pass  # pragma: no cover


def test_invalid_dict():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Dict[str, Item] = Query(default=None)):
            pass  # pragma: no cover
