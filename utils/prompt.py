from langchain_core.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector


from template.prompttemplate import basic_template, context_template, fewshot_template
from template.fewshotstemplate import example_template, examples

basic_prompt = PromptTemplate.from_template(basic_template)

context_prompt = PromptTemplate.from_template(context_template)

fewshot_prompt = PromptTemplate.from_template(fewshot_template)

example_prompt = PromptTemplate(
    input_variable=["query", "answer"],
    template = example_template
)

# now break our previous prompt into a prefix and suffix
# the prefix is our instructions
prefix = """The following are exerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative  and funny responses to the users questions. Here are some
examples: 
"""
# and the suffix our user input and output indicator
suffix = """
User: {query}
AI: """

# now create the few shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n"
)

# To control the length of the examples we can use an example selector instead of passing the examples directly to the FewShotPromptTemplate
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50  # this sets the max length that examples should be
)

# We then pass our example_selector to the FewShotPromptTemplate to create a new — and dynamic — prompt template:

# now create the few shot prompt template
dynamic_prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,  # use example_selector instead of examples
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n"
)