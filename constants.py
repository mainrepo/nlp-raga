import os
import pickle
import logging

delimiter = "####"
end_of_chat = "please do visit again"
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
logging.basicConfig(level=logging.INFO)
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

logger = logging.getLogger('bot-service')

file_name: str = "customer_service.pkl"
customer_service: str = ""
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        customer_service = pickle.load(file)


file_name: str = "pizza_order.pkl"
pizza_order: str = ""
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        pizza_order = pickle.load(file)