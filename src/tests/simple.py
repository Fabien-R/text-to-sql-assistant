import pytest
from textwrap import dedent

from src.adapters.agent.crew.crews import DBCrew
from src.domain.model import UserInput


@pytest.fixture
def catalog() -> UserInput:
    return UserInput(
        dedent("""
        CREATE TABLE `authors` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `first_name` VARCHAR(50) NOT NULL COLLATE 'utf8_unicode_ci',
        `last_name` VARCHAR(50) NOT NULL COLLATE 'utf8_unicode_ci',
        `email` VARCHAR(100) NOT NULL COLLATE 'utf8_unicode_ci',
        `birthdate` DATE NOT NULL,
        `added` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `email` (`email`)
);

        CREATE TABLE `posts` (
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `author_id` INT(11) NOT NULL,
            `title` VARCHAR(255) NOT NULL COLLATE 'utf8_unicode_ci',
            `description` VARCHAR(500) NOT NULL COLLATE 'utf8_unicode_ci',
            `content` TEXT NOT NULL COLLATE 'utf8_unicode_ci',
            `date` DATE NOT NULL,
            PRIMARY KEY (`id`)
        );
        """)
    )


@pytest.fixture
def user_question() -> UserInput:
    return UserInput("""What is the average number of posts that have been written by the 3 most prolific authors?""")


def test_crew_agent_to_convert_simple_question_on_simple_catalog(user_question, catalog):
    db_crew = DBCrew(user_question=user_question, catalog=catalog)
    response = db_crew.execute()
    print(response)
    # TODO how to test llm answer?
    assert response.__contains__("author")
