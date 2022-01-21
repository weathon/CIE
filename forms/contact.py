from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

templete = """
Name: %s
E-mail: %s
WeChat ID: %s
Age: %s
Course: %s
Comment: %s
"""

class Contact(BaseModel):
    Name: str
    Email: str
    WeChatID: str
    Age: str
    Course: str
    Comment: str

import smtplib, ssl
def send(message):
        
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "risaxu0727@gmail.com"
    password = "Qian-610951"


    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, "risaxu0727@gmail.com", message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

@app.post("/contact.py")
def read_item(item: Contact ):
    # try:

        ans = str(item).replace("' ","\n")
        with open("All Students.txt","a") as f:
            f.write("\n--------------------\n")
            f.write(ans)
        send(ans)
        return "提交成功，请耐心等待回复。"
    # except:
    #     return "提交失败，请重试。"