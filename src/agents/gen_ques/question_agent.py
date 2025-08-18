from src.model.model import llm
from src.templates.prompts import question_template

question_chain = question_template | llm


