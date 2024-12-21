from langchain import PromptTemplate


template = """Question : {question}

Answer : """

prompt_template = PromptTemplate(
                  template = template,
                  input_variable = ['question']
                  )

# user question

Question = "What is the capital of France?"