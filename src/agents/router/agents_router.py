from langchain_core.prompts import PromptTemplate
from pathlib import Path
import sys
project_folder = Path(__file__).resolve().parents[3]
sys.path.append(str(project_folder))
from src.model.model import llm
from src.agents.router.llm_router import router_chain
from src.agents.gen_ques.question_agent import question_agent

agent_router ={
    "ask_question_agent": question_agent,
}
def route_take(message):
    category = router_chain.invoke({"input":message})
    if 'ask_question' in category.content:
        ask_question = agent_router.get(ask_question_agent)
        question = ask_question.invoke({"input":})
    
