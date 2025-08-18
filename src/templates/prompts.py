from langchain_core.prompts import PromptTemplate
question_prompt ="""
You are a technical Interviewe.  Generate one interview question based on the knowledge base for the field
: {field}

Make it clear and concise
"""
question_template = PromptTemplate.from_template(template=question_prompt)

eval_prompt = """
you are an evaluator.
compare the candidate answer with the reference answer from the knowledge base.
question: {question}
candidate answer : {answer}
reference: {reference}
Score from 1-10 and explain briefly
"""
eval_template = PromptTemplate.from_template(template=eval_prompt)
router_prompt = """
Your are the interview flow router.
Given the conversation so far, decide what to do next:
- ask_question
- evaluate_answer
- follow_up
return only one option

conversation so far: {history}

"""
router_template = PromptTemplate.from_template(template=router_prompt)

