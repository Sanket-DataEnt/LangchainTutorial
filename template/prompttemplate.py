
basic_template = """Question : {question}

Answer: 

Instructions: give the exact answer to the question without providing additional information and if \
    you don't know the answer, please respond with "I do not know"."""

context_template = """Answer the question based on the context below. 

Instructions : If the question cannot be answered using the Context information provided answer with "I don't know".

Context: Large Language Models (LLMs) are the latest models used in NLP.
Their superior performance over smaller models has made them incredibly
useful for developers building NLP enabled applications. These models
can be accessed via Hugging Face's `transformers` library, via OpenAI
using the `openai` library, and via Cohere using the `cohere` library.

Question: {question}

Answer: """

# Which libraries and model providers offer LLMs?

