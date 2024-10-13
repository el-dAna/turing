# main.py
# Importing FastAPI framework
from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a GET endpoint to retrieve an item by its ID
# The path parameter 'item_id' is an integer
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Return the item ID as part of a JSON response
    return {"item_id": item_id}

# Define a POST endpoint to create a new item
# The request body expects a dictionary (JSON object)
@app.post("/items/")
async def create_item(item: dict):
    # Return the created item in the response
    return {"item": item}
