from src.templates.prompts import eval_template
from src.model.model import llm

eval_chain = eval_template | llm
