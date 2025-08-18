from pathlib import Path
import sys
project_folder = Path(__file__).resolve().parents[2]
sys.path.append(str(project_folder))
from src.data.load_kb import load_kb
from src.agents.gen_ques.question_agent import question_chain
from src.agents.eval_agent.eval_agent import eval_chain
from src.agents.router import llm_router
from src.memory.conversation import ConversationMemory

def start_interview(field):
    retriever = load_kb()
    memory = ConversationMemory()
    q = question_chain.invoke({"field":field})
    question_content = q.content
    memory.add("interviewer", question_content)
    print(f"Interview question: {question_content}")

    answer = input("Type your answer here ....")
    memory.add("candidate",answer)

    docs = retriever.get_relevant_documents(question_content)
    reference = docs[0].page_content if docs else "No reference found use your common knowledge"

    evaluation = eval_chain.invoke({"question":question_content, "answer":answer,"reference":reference})
    memory.add("evaluation", evaluation.content)

    print(f"Evaluation: {evaluation.content}")

if __name__ =="__main__":
    field = input("name of field to do interview in ")
    start_interview(field)