from fastapi import FastAPI, Request, Form, APIRouter
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


router = APIRouter(
        prefix="/contact",
        tags=["contact"]
        )


def send(name,mail,message):

    msg=MIMEMultipart()
    msg['Subject'] = f'{name} wants to say hi'
    msg['From'] = 'loggerk420@gmail.com'
    message=f'{name}:\n<{mail}>\n\n{message}'
    text = MIMEText(str(message))
    msg.attach(text)
    s = smtplib.SMTP('smtp.gmail.com', '587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('loggerk420@gmail.com','citwroufjzvyeqrk')
    s.sendmail('loggerk420@gmail.com', 'andrijajovanovic001@gmail.com', msg.as_string())
    s.quit()

@router.get("/counter")
def get_message_count(request: Request):

    return {'message':'this is contact response, here I will add contact endpoint that will be used to process POST requests from react frontend', 'count of messages':cnt}



@router.post('/send')
async def send_mail(request: Request,name: str = Form(...), email: str = Form(...), message:str = Form(...)):
    print('#BEGGIN EMAIL')
    print(f'name:\t\t{name}\nemail:\t\t{email}\nmessage:\t\t{message}\n')
    print('#END EMAIL')
    send(name,email, message)
    return {'response':'form sent succesfully'}
