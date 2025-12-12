import json
import boto3
import urllib.parse
from datetime import datetime
import base64
import uuid

# DynamoDB client
dynamodb_client = boto3.client("dynamodb")
TABLE_NAME = "dee-table"

def lambda_handler(event, context):
    try:
        print("Event:", json.dumps(event))

        http_method = event.get("httpMethod", "")

        if http_method == "GET":
            return serve_contact_page()

        elif http_method == "POST":
            return handle_form_submission(event)

        else:
            return error_response(405, "Method Not Allowed")

    except Exception as e:
        print("ERROR:", str(e))
        return error_response(500, f"Internal Server Error: {str(e)}")


# Serve HTML page
def serve_contact_page():
    try:
        with open("contactus.html", "r", encoding="utf-8") as f:
            html = f.read()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html",
                "Access-Control-Allow-Origin": "*"
            },
            "body": html
        }

    except Exception as e:
        raise Exception(f"Could not load contactus.html: {str(e)}")


# Handle POST request
def handle_form_submission(event):
    body = event.get("body", "")

    if event.get("isBase64Encoded"):
        body = base64.b64decode(body).decode("utf-8")

    if not body:
        raise Exception("POST body is empty.")

    parsed = urllib.parse.parse_qs(body)
    print("Parsed form data:", parsed)

    # EXACTLY same as your HTML names
    name = parsed.get("name", [""])[0]
    email = parsed.get("email", [""])[0]
    message = parsed.get("message", [""])[0]

    submission_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    # Insert into DynamoDB
    try:
        dynamodb_client.put_item(
            TableName=TABLE_NAME,
            Item={
                "id": {"S": submission_id},
                "name": {"S": name},
                "email": {"S": email},
                "message": {"S": message},
                "timestamp": {"S": timestamp}
            }
        )
        print("Inserted into DynamoDB:", submission_id)

    except Exception as e:
        print("DynamoDB ERROR:", str(e))
        raise Exception("DynamoDB ERROR: " + str(e))

    # HTML success response
    html = f"""
    <html>
    <body>
        <h1>Thank you, {name}!</h1>
        <p>Your message has been submitted successfully.</p>
        <p>Submission ID: {submission_id}</p>
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": html
    }


# Error response
def error_response(status_code, message):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "text/plain",
            "Access-Control-Allow-Origin": "*"
        },
        "body": message
    }
