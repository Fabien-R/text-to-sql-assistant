from textwrap import dedent

from src.domain.model import UserInput


def column_retriever_prompt(user_question: UserInput, catalog: UserInput):
    return dedent(
        f"""You will extract the tables and columns required to answer the user's question.
        ### Question
        {user_question}
        ### Columns catalog
        {catalog}
        Select the most representative columns to answer the question and do not exceed 10 columns.
        Each column should be prefixed by the table name.
        No other column should appear in your response.
        #### Example
        - table1.column_11
        - table2.column_21
        - table2.column_22
        - table3.column_31
        - table3.column_32
        """
    )


def question_transcriber_prompt(user_question: UserInput):
    return dedent(
        f"""Using the extracted columns, you will now transcribe the user's question into natural language. Restrict your answer to the most relevant columns.
        Reason step by step. 
        ### Question {user_question}
        Your final answer should be your transcription of the user's question into natural language, 
        only your transcription of the user's question in natural language and nothing else.
        """
    )


def sql_translator_prompt(
        user_question: UserInput, catalog: UserInput
):
    return dedent(
        f"""Using the transcribed user's question and the extracted columns, you will now create a SQL query.
        ### Question
        {user_question}
        ### Columns catalog
        {catalog}
        ### Constraint
        Your final answer should be a SQL query that
        - answers the user's question
        - is correct and executable
        - does not use * in any SELECT statement (even the wrapped ones)
        = every column should be prefixed by the table name
        
        If you are not able to answer the question with the given columns catalog, return 'I don't know.'.
        """
    )
