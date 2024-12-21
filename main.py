from auth.config import HUGGINGFACEHUB_API_TOKEN
from utils.logger import logger
from template.prompttemplate import prompt
from langchain_huggingface import HuggingFaceEndpoint
import time

import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN


# logger.info(f"API token: {HUGGINGFACEHUB_API_TOKEN}")

# # initialise Hub LLM
# hub_llm = HuggingFaceHub(
#     repo_id='google/flan-t5-xl',
#     model_kwargs={'temperature':1e-10,}
# )

# initialise HuggingFaceEndpoint
hub_llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    temperature=0.5,
    max_length=128,
    huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN
    )


# initialise LLMChain
llm_chain = prompt | hub_llm

# single question
single_question = "What is the capital of France?"

# multi questions

multiple_questions = [
    {"question": "What is the capital of France?"},
    {"question": "What is the capital of Germany?"},
    {"question": "What is the capital of Italy?"},
]

# # generate answer
response = llm_chain.invoke({"question": single_question})

# generate multiple answers

for question in multiple_questions:
    start_time = time.time()
    multiple_response = llm_chain.invoke(question)
    logger.info(f"Multiple RESPONSE : {multiple_response}, Time taken: {(time.time() - start_time):.2f} seconds")

# logger.info(f"RESPONSE : {response}")
