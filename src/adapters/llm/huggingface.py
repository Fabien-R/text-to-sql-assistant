from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


def get_llm():
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="text-generation",
        temperature=0.01,
        max_new_tokens=8196,
    )
