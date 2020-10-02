'''
Name: leftovers.py
Description: lambda function for finding query strings in input and sending
    emails when query is found.
Author: David J Wehrlin
Exceptions:
    EmailAuthenticationFailed: failed authentication to gmail email
Functions:
    lambda_handler: handles lambda http input and maybe sends email if query
        found in input string.
'''
from twilio.rest import Client
import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def lambda_handler(event, context):
    '''Takes in an byte array and convets to string, then checks for queries in
    string and sends email if a query is found.'''
    if event is None or context is None:
        raise ValueError("Event or context is None")
    string = str(base64.b64decode(event['body']))
    found_queries = []
    for query in os.environ['QUERY_LIST'].split(','):
        if string.find(query) != -1:
            found_queries.append(query)
    # If query found then send email
    if len(found_queries) > 0:
        from_address = os.environ["FROM_ADDRESS"]
        from_password = os.environ["FROM_PASSWORD"]
        to_address = os.environ["TO_ADDRESS"]
        message = MIMEMultipart()
        message['From'] = from_address
        message['To'] = to_address
        subject = ""
        for query in found_queries:
            subject += query
            subject += " "
        message['Subject'] = 'Leftover Tag Found: ' + subject
        message.attach(MIMEText("https://www.cpwshop.com/licensing.page\n"))
        for query in found_queries:
            message.attach(MIMEText(f"{query}\n"))
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        try:
            session.login(from_address, from_password)
            text = message.as_string()
            session.sendmail(from_address, to_address, text)
        except:
            print("<<Error Sending Email Message>>")
            raise
        finally:
            session.quit()

        account_sid = os.environ['TWILIO_SID']
        auth_token = os.environ['TWILIO_AUTH']
        client = Client(account_sid, auth_token)
        body = ""
        for query in found_queries:
            body += query
            body += "\n"
        message = client.messages \
                        .create(
                            body="https://www.cpwshop.com/licensing.page\nQuery found\n" + body,
                            from_=str(os.environ['FROM_PHONE']),
                            to=str(os.environ['TO_PHONE'])
                        )
        return {
            'statusCode': 200,
            'body': "\nQuery Found!\n"
        }
    return {
        'statusCode': 404,
        'body': "\nNot Found!\n"
    }