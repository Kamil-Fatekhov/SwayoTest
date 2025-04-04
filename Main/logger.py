import logging
from datetime import datetime
from typing import Dict, Any


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('sms_service.log'),
            logging.StreamHandler()
        ]
    )

def log_request(sender: str, recipient: str, message: str) -> None:
    logging.info(f"Sending SMS - From: {sender}, To: {recipient}, Message: {message[:20]}...")

def log_response(status_code: int, response_body: str) -> None:
    logging.info(f"Received response - Status: {status_code}, Body: {response_body}")

