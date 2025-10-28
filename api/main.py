from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample facts list
facts = [
    "The first computer programmer was a woman named Ada Lovelace",
    "The first computer mouse was made of wood",
    "The first website is still online",
    "The term 'bug' in computing came from an actual moth",
    "JavaScript was created in just 10 days",
    "The heart of a shrimp is located in its head.",
    "A snail can sleep for three years.",    
    "Slugs have four noses.",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts."
]

# Data in this example is stored as a variable, in memory.
# This data will be erased with every restart of the server;
# might even be reset in between calls to the back-end.
# So this is not a proper, permanent and persistent store of data.
# For that we need to use a database, as we'll see next week.

data_list = []  # list to store strings; empty to start 

# --- GET Endpoint ---
@app.get("/items")
def get_items():
    """
    Fetches the entire list of items.
    """
    # Simply return the list
    return {"items": data_list}

# --- POST Endpoint --- 
@app.post("/item")
def add_item(itemId = Body(...), itemText = Body(...)):
    """
    Adds an item to the list.    
    """
    if not itemId or not itemText:
        # Basic validation
        raise HTTPException(status_code=400, detail="Item id and text must be passed")
        
    itemDict = { "id":itemId,"text":itemText}    
    data_list.append(itemDict)
    
    # Return a success message and the item that was added
    return {"message": "Item added successfully", "item": itemDict }

# Basic root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "backend server is listening..."}

@app.get("/random-fact")
async def get_random_fact():
    return {"fact": random.choice(facts)}