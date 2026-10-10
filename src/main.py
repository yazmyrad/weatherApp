from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uvicorn

app = FastAPI()
# Todo Pydantic schema for validating user phone number
@app.get('/')
def root():
    return "Hi mate"

if __name__=='__main__':
    uvicorn.run("main:app", reload=True)