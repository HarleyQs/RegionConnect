from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api
# App Object
app = FastAPI()
origins = ['*', 'https://cc84-180-252-125-38.ngrok-free.app']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api.router)



@app.get('/')
def root_api():
    return {"messagee": "Welcome to Wilayah Indonesia"}

