import json
import base64

def encode(username:str, password: str, sender: str, recipient: str, message: str):
    request_data = {
        "sender":sender,
        "recipient":recipient,
        "message":message
    }
    json_data = json.dumps(request_data)
    auth = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode()
    return json_data, auth