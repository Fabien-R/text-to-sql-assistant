
if __name__ == "__main__":
    print("Hey there! I'm your text to sql ai-assistant")
    print("I will help you generate a sql query from your natural language question")

    print("###################################################################################")
    data_catalog_input: str = input("Please provide the data sources description on which we need to generate the sql query\n")
    print(data_catalog_input)
    question_input: str = input("Please provide the question you want to ask\n")
    print(question_input)