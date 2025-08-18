from langchain_core.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain
from src.model.model import llm


router_chain = router_prompt | llm