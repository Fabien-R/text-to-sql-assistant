from crewai import Crew

from src.adapters.agent.crew.agents import SQLAgents
from src.adapters.agent.crew.tasks import retrieve_columns_task, transcribe_question_task, translate_sql_task
from src.domain.agent.DBAssistant import DBAssistant
from src.domain.model import UserInput, SQLQuery
from crewai.process import Process


class DBCrew(DBAssistant):
    def __init__(self, user_question: UserInput, catalog: UserInput):
        super().__init__(
            user_question = user_question,
            catalog = catalog,
        )

    def execute(self) -> SQLQuery:
        # Agents
        domain_expert = SQLAgents.DOMAIN_EXPERT.value
        sql_engineer = SQLAgents.SQL_ENGINEER.value

        # Tasks
        tasks = [
            retrieve_columns_task(
                agent=domain_expert,
                user_question=self.user_question,
                catalog=self.catalog,
            ),
            transcribe_question_task(
                agent=domain_expert,
                user_question=self.user_question,
            ),
            translate_sql_task(
                agent=sql_engineer,
                user_question=self.user_question,
                catalog=self.catalog
            ),
        ]

        crew = Crew(
            agents=[domain_expert, sql_engineer],
            tasks=tasks,
            process=Process.sequential,
            verbose=False,
        )

        return SQLQuery(crew.kickoff())
