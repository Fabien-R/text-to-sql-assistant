from crewai import Agent, Task

from src.domain.model import UserInput
from src.domain.prompts.catalog import column_retriever_prompt, question_transcriber_prompt, sql_translator_prompt


def retrieve_columns_task(agent: Agent, user_question: UserInput, catalog: UserInput):
    return Task(
        description=column_retriever_prompt(user_question, catalog),
        agent=agent
    )


def transcribe_question_task(agent: Agent, user_question: UserInput):
    return Task(
        description=question_transcriber_prompt(user_question),
        agent=agent
    )


def translate_sql_task(agent: Agent, user_question: UserInput, catalog: UserInput):
    return Task(
        description=sql_translator_prompt(user_question, catalog),
        agent=agent
    )
