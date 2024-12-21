from langchain_core.prompts import PromptTemplate


template = """Question : {question}

Answer: 

Instructions: give the exact answer to the question without providing additional information"""

# prompt = PromptTemplate(
#         template = template,
#         input_variables = ['question']
#         )

prompt = PromptTemplate.from_template(template)
