from fastapi import FastAPI, HTTPException
from models import Items
from typing import List

app = FastAPI()

items_db: List[Items] = []

@app.get('/items', response_model=List[Items])
def get_items():
    return items_db


@app.get('/items/{item_id}', response_model=Items)
def get_item_by_id(item_id: str):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            return items_db[index]
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post('/addItem', response_model=Items)
def add_item(new_item: Items):
    for index, item in enumerate(items_db):
        if item.id == new_item.id:
            raise HTTPException(status_code=400, detail="Item already present")
    items_db.append(new_item)
    return new_item


@app.put('/updateItem', response_model=Items)
def update_item(updated_item: Items):
    for index, item in enumerate(items_db):
        if item.id == updated_item.id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=400, detail="Item already present")


@app.delete('/delete/{item_id}')
def delete_item(item_id: str):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"message": "Item has been deleted."}
    raise HTTPException(status_code=400, detail="Item not present")

