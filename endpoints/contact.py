
from fastapi import FastAPI, Request, Form, APIRouter
import os



router = APIRouter(
        prefix="/contact",
        tags=["contact"]
        )

@router.get("/")
def contact(request: Request):
    return {'message':'this is profile page'}
