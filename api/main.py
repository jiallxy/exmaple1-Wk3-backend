from fastapi import FastAPI
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

@app.get("/")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."

@app.get("/random-fact")
async def get_random_fact():
    return {"fact": random.choice(facts)}