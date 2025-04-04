import argparse
import tomllib
import socket

from make_url import *
from encode import *
from make_requests import *
from logger import *

def handling():
    setup_logging()
    parser = argparse.ArgumentParser(description="sms handling")
    parser.add_argument("sender_number", type=str, help="Input sender`s number")
    parser.add_argument("recipient_number", type=str, help="Input recipient`s number")
    parser.add_argument("message", type=str, help="Input message")

    args = parser.parse_args()

    sender = args.sender_number
    recipient = args.recipient_number
    message = args.message

    try:
        with open("config.toml", "rb") as file:
            config = tomllib.load(file)
    except FileNotFoundError:
        print("File doesnt find")
        return

    url = config["server"]["website"]
    username = config["user"]["username"]
    password = config["user"]["password"]


    json_data, auth = encode(username, password, sender, recipient, message)

    protocol, host,port, path = make_url(url)
    request = HTTPRequest(
        method="POST",
        path=path,
        headers={
            "Host": host,
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/json",
            "Content-Length": str(len(json_data.encode('utf-8'))),
            "Connection": "close"
        },
        body=json_data
    )

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        print("Connected")

    except socket.timeout:
        print("Error")

    except socket.error as error:
        print(f"Error: {error}")

    try:
        log_request(sender, recipient, message)
        s.sendall(request.to_bytes())
        response = HTTPResponse.from_bytes(s.recv(4096))
        log_response(response.status_code, response.body)
        print(f"Status: {response.status_code}\nBody: {response.body}")

    except socket.error as error:
        print("Socket error", error)

    finally: s.close()