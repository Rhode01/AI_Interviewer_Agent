from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
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
Your are the interview flow router. responsible for starting an interview, etc ... if you have a conversation history 
Given the conversation so far, decide what to do next:
- ask_question (generate_question)
- evaluate_answer
- follow_up
return only one option

conversation so far: {input}

"""
router_template = PromptTemplate.from_template(template=router_prompt)
gen_question_prompt ="""
You are a technical interviewer for the field: {field}.
Use ONLY the company knowledge base context below to craft ONE clear, concise interview question.
The question must be answerable from the context (no outside knowledge). Prefer high-signal, role-relevant topics.

[Knownledge base]
 {context}

Return just the question text. No preface, no bullets.
        """.strip()

gen_quest_prompt_template = PromptTemplate.from_template(gen_question_prompt)