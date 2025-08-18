from langchain_core.prompts import PromptTemplate
question_prompt ="""
You are a technical Interviewe.  Generate one interview question based on the knowledge base for the field
: {field}

Make it clear and concise
"""
question_template = PromptTemplate.from_template(template=question_prompt)