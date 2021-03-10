
from fastapi import FastAPI, Request, Form, APIRouter
import os



router = APIRouter(
        prefix="/contact",
        tags=["contact"]
        )

@router.get("/")
def contact(request: Request):
    return {'message':'this is contact response, here I will add contact endpoint that will be used to process POST requests from react frontend'}
