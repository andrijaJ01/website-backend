from fastapi import FastAPI
from backend.endpoints import contact,about
#from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware

from typing import Optional

app = FastAPI(redoc_url='/documentation')
#app.add_middleware(HTTPSRedirectMiddleware)

origins = [
"http://localhost:3000",
"http://127.0.0.1:3000",
"http://192.168.1.10:3000"]
app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["GET","POST"],
            allow_headers=["*"],
                            )



app.include_router(contact.router)
app.include_router(about.router)

@app.get('/')
async def get_root():
    return{'message':'root of the backend'}
