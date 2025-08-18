from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnableLambda

from langchain_core.prompts import PromptTemplate
from pathlib import Path
import sys
project_folder = Path(__file__).resolve().parents[3]
sys.path.append(str(project_folder))
from src.model.model import llm
from src.agents.router.llm_router import router_chain


technical_template ="Your are a technical interviewer. Ask technical questions relavant to the candidates role. {message}"
behaviour_template = "Your are a Behaviour interviewer. Focus on soft skills and culture  {message}"
hr_template = "You are an"
follow_up_tempate ="you are a follow up Agent. ask deeper questions to clarify answers candidates response {message}"


technical_chain = PromptTemplate.from_template(template=technical_template)| llm
behaviour_chain = PromptTemplate.from_template(template=behaviour_template) | llm
hr_chain = PromptTemplate.from_template(template=hr_template)| llm
follow_up_chain = PromptTemplate.from_template(template=follow_up_tempate) | llm


agent_router ={
    "technical": technical_chain,
    "behaviour": behaviour_chain,
    "hr": hr_chain,
    "follow_up": follow_up_chain

}
def route_take(message):
    category = router_chain.invoke({"message":message})
    chain = agent_router.get(category.content)
    if chain:
        response  = chain.invoke({"message": message})
        return response.content
    else:
        return f"No agent found for category : {category}"
    

if __name__ == "__main__":
    input_ = input("What category")
    print(route_take(message=input_))