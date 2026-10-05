from fastapi import FastAPI
from pydantic import BaseModel

class UserInput(BaseModel):
    input:str

app=FastAPI(title="Data Science Docker Demo")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/output")
def output(input_data:UserInput):
    print("The user input is: ",input_data.input)


@app.get("./")
def root():
    return {"message: This FastAPI and Docker demo. Post to /output with a message"
            "example_body":"print something"}