from langchain_core.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain
from src.model.model import llm
router_template = """
You are the  LLLm router for an Ai interview system.
classify the following candidate message into exactly one category:
- technical
- behaviour
- hr
- follow_up
candidate message : {message}

return only the category name.

"""
router_prompt = PromptTemplate(template=router_template, input_variables=['message'])

router_chain = router_prompt | llm