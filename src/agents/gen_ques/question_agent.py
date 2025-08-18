from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from src.model.model import llm
from src.templates.prompts import gen_quest_prompt_template

def _format_docs(docs, max_chars=4000):
    text = "\n\n".join(d.page_content.strip() for d in docs if d.page_content)
    return text[:max_chars]

def build_question_chain(retriever):
    

    chain = {
        "field": itemgetter("field"),
        "context": itemgetter("field") | retriever | RunnableLambda(_format_docs),
    } | gen_quest_prompt_template | llm | StrOutputParser()

    return chain
