from enum import Enum

from crewai import Agent
from textwrap import dedent

from src.adapters.llm.huggingface import get_llm


class SQLAgents(Enum):
    DOMAIN_EXPERT = Agent(
        role="Domain expert",
        goal="Transcribes the user's question and columns information into natural language so that an SQL engineer can understand it.",
        backstory=
            dedent(
                """You are an experienced analyst with a broad knowledge that allows you to translate any user question into expert domain question."""
            ),
        allow_delegation=False,
        verbose=False,
        llm=get_llm()
    )

    SQL_ENGINEER = Agent(
        role="Seasoned SQL Engineer",
        goal="Create a correct and executable sql query from a question of an export",
        backstory=
            dedent(
                """You are an experienced SQL engineer at a data platform hosting the user data.
                You do your best to create a perfect and high-performance SQL query that answers expert question.
                """
            ),
        allow_delegation=False,
        verbose=False,
        llm=get_llm()
    )