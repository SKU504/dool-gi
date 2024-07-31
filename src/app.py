import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

class Chatbot:
    # initalize Chatbot object.
    def __init__(self):
        # initialize api key and model
        with open("api_key") as key:
            os.environ["OPENAI_API_KEY"] = key.read().strip()
        model = ChatOpenAI(model="gpt-4")

        # TODO

        # initialize object
        self.model = model;

    # talk to the chatbot
    #
    # str: question from user.
    # return: answer from AI.
    def talk(self, msg: str) -> str:
        # TODO
        return msg;
