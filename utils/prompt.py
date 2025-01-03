from langchain_core.prompts import PromptTemplate
from template.prompttemplate import basic_template, context_template, fewshot_template

basic_prompt = PromptTemplate.from_template(basic_template)

context_prompt = PromptTemplate.from_template(context_template)

fewshot_prompt = PromptTemplate.from_template(fewshot_template)