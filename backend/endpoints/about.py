
from fastapi import FastAPI, Request, Form, APIRouter
import os



router = APIRouter(
        prefix="/about",
        tags=["about"]
        )

data={
'title':'Who am I?',
'description':'I am freelance, self-educated, highly motivated, python developer from Serbia and I’ve been coding for 1 year with multiple years of supporting education.I usually work on building web scrapers,FastAPI or Flask web apps and all kinds of automatization.$My primary concentration at the moment is python and have a firm understanding of HTML, CSS and Javascipt.I am comfortable with working on both Windows and Linux operating systems. To help enhance and support my graphics projects I often work with GIMP and Inkscape.'
}
@router.get("/")
def about_me(request: Request):
    return data
