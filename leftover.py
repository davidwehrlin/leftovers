import json
from time import time
import requests
import pdfplumber
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client

def leftover_function(event, context):
    
    # DOWNLOADS PDF FILE 
    print("Downloading PDF")
    start = time()
    url = "https://gahp.net/wp-content/uploads/2017/09/sample.pdf"
    response = requests.get(url, allow_redirects=True)
    with open("/tmp/leftover-list.pdf", "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f"Time to Download: {time() - start}")

    # Analyzing PDF for Query Results
    print("Analyzing PDF ...")
    start = time()
    isIncluded = False
    with pdfplumber.open("/tmp/leftover-list.pdf") as f:
        i = 0
        for page in f.pages:
            i += 1
            print(f"Extracting Page {i}")
            s = page.extract_text()
            if (s.find(os.environ["QUERY_STRING"]) != -1):
                print("Found Query String in PDF!!!")
                isIncluded = True
                break
    print(f"Time to Analyze: {time() - start}")
    
    if (isIncluded):
        print("Sending Email Message ...")
        start = time()
        #The mail addresses and password
        from_address = os.environ["FROM_ADDRESS"]
        from_password = os.environ["FROM_PASSWORD"]
        to_address = os.environ["TO_ADDRESS"]
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = from_address
        message['To'] = to_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(f"Query found in leftovers list", 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(from_address, from_password) #login with mail_id and password
        text = message.as_string()
        session.sendmail(from_address, to_address, text)
        session.quit()
        print(f"Time to Send Email Message: {time() - start}")

        print("Sending Text Message ...")
        start = time()
        client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_AUTH"])
        client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=os.environ["FROM_PHONE"],
                     to=os.environ["TO_PHONE"]
                 )
        print(f"Time to Send Text Message: {time() - start}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully handled timer event!')
    }
