from langchain_core.prompts import PromptTemplate


template = """Question : {question}

Answer: give the exact answer"""

# prompt = PromptTemplate(
#         template = template,
#         input_variables = ['question']
#         )

prompt = PromptTemplate.from_template(template)
