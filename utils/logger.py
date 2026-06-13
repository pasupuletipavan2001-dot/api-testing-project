import logging

logging.basicConfig(
    filename="logs/api_test.log",
    level=logging.INFO
)

def log_message(message):
    logging.info(message)