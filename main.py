from auth.config import HUGGINGFACEHUB_API_TOKEN
from utils.logger import logger
from template.prompttemplate import prompt
# from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
# from langchain_community.llms import HuggingFaceLLM
from langchain.chains import LLMChain

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

question = "What is the capital of France?"

# # generate answer
response = llm_chain.invoke({"question": question})
logger.info(f"RESPONSE : {response}")