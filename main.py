from auth.config import HUGGINGFACEHUB_API_TOKEN
from utils.logger import logger
from utils.prompt import basic_prompt
from langchain_huggingface import HuggingFaceEndpoint
import time

# import os

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN


# initialise HuggingFaceEndpoint
hub_llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    temperature=0.5,
    max_new_tokens=128,
    huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN
    )


# initialise LLMChain
llm_chain = basic_prompt | hub_llm

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
    logger.info(f"Multiple BASIC RESPONSE : {multiple_response}, Time taken: {(time.time() - start_time):.2f} seconds")

# Context question
context_correct_question = "Which libraries and model providers offer LLMs?"
context_response = llm_chain.invoke({"question": context_correct_question})
logger.info(f"CONTEXT CORRECT RESPONSE : {context_response}")

context_wrong_question = "What is the capital of India?"
context_response = llm_chain.invoke({"question": context_wrong_question})
logger.info(f"CONTEXT WRONG RESPONSE : {context_response}")

### To work on optimizing the prompt to answer with context information only. Currently the model is not able to answer the question based on the context information provided.




