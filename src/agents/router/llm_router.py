from langchain_core.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain
from src.model.model import llm
from src.templates.prompts import router_template


router_chain = router_template | llm