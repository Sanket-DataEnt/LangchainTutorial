
basic_template = """Question : {question}

Answer: 

Instructions: give the exact answer to the question without providing additional information and if \
    you don't know the answer, please respond with "I do not know"."""

# context_template = """Answer the Question : {question} based on the context below ONLY. 

# Instructions: Give the exact answer to the question based on the Context information provided.

# Context: Large Language Models (LLMs) are the latest models used in NLP.
# Their superior performance over smaller models has made them incredibly
# useful for developers building NLP enabled applications. These models
# can be accessed via Hugging Face's `transformers` library, via OpenAI
# using the `openai` library, and via Cohere using the `cohere` library.

# IMPORTANT NOTE : If the question cannot be answered using the Context information provided answer with "I don't know".

# Answer: """

context_template = """ Question : {question} 

Answer:

Context: Large Language Models (LLMs) are the latest models used in NLP. Their superior performance over smaller models has made them incredibly useful for developers building NLP enabled applications. These models can be accessed via Hugging Face's `transformers` library, via OpenAI using the `openai` library, and via Cohere using the `cohere` library.

Instructions: Give the exact answer to the {question} based on the Context information provided above.

NOTE: If the question cannot be answered using the Context information provided, answer with "I don't know".


"""

# Which libraries and model providers offer LLMs?

