from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from src.model.model import llm
from src.templates.prompts import gen_quest_prompt_template
from langgraph.prebuilt import create_react_agent
from langchain_core.documents import Document

def _format_docs(docs:Document, max_chars:int=4000):
    text = "\n\n".join(d.page_content.strip() for d in docs if d.page_content)
    return text[:max_chars]

def build_question_chain(retriever):
    chain = {
        "field": itemgetter("field"),
        "context": itemgetter("field") | retriever | RunnableLambda(_format_docs),
    } | gen_quest_prompt_template | llm | StrOutputParser()

    return chain


question_agent_exec = create_react_agent(model=llm,prompt=gen_quest_prompt_template, tools= [])
    