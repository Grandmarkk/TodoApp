from fastapi import FastAPI, Response

# configure fastapi
app = FastAPI()

# API
@app.get("/")
def awsome_api():
    """
    A simple API that returns a message.
    """
    return Response("Hello!")