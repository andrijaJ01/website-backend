from fastapi import FastAPI
from backend.endpoints import contact,about
#from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware

from typing import Optional

app = FastAPI(redoc_url='/documentation')
#app.add_middleware(HTTPSRedirectMiddleware)

origins = [
        "https://www.andrijajovanovic.ml",
        "http://localhost:3000",
        "http://192.168.1.10:3000",
        "https://192.168.1.10:3000",
        "https://www.andrijajovanovic.ml",
        "https://andrijajovanovic.ml",
        "https://mystifying-bassi-d50963.netlify.app/"
        ]
app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["GET","POST"],
            allow_headers=["*"],
                            )

data={
        'name':'Andrija Jovanovic',
        'text':'fullstack developer'
        }

app.include_router(contact.router)
app.include_router(about.router)

@app.get('/')
async def get_root():
    return data
