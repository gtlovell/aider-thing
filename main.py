from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# A list of dad jokes
dad_jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!",
]

class Joke(BaseModel):
    joke: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Dad Jokes API!"}

@app.get("/joke", response_model=Joke)
async def get_joke():
    return {"joke": random.choice(dad_jokes)}

@app.get("/jokes", response_model=list[Joke])
async def get_all_jokes():
    return [{"joke": joke} for joke in dad_jokes]
