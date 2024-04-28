from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Vercel!"}

# ... more routes and logic for your FastAPI app
