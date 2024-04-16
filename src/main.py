from src.adapters.agent.crew.crews import DBCrew
from src.domain.model import UserInput


def multi_input(message: str) -> str:
    print(message)
    contents = []
    while True:
        line = input()
        if not line.strip():
            break
        contents.append(line)
    return "\n".join(contents)


if __name__ == "__main__":
    print("Hey there! I'm your text to sql ai-assistant")
    print("I will help you generate a sql query from your natural language question")

    print("###################################################################################")
    data_catalog_input = UserInput(multi_input("Please provide the data sources description on which we need to generate the sql query"))
    question_input = UserInput(input("Please provide the question you want to ask\n"))
    db_crew = DBCrew(user_question=question_input, catalog=data_catalog_input)
    print(db_crew.execute())
