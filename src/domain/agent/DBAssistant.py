from abc import ABC, abstractmethod
from src.domain.model import UserInput, SQLQuery


class DBAssistant(ABC):
    """ This class is the interface for the assistant responsible to translate a user question into sql query"""

    def __init__(self, user_question: UserInput, catalog: UserInput):
        self.user_question = user_question
        self.catalog = catalog

    @abstractmethod
    def execute(self) -> SQLQuery:
        """ The main method to translate the user initial question into a sql query"""
        raise NotImplementedError()
