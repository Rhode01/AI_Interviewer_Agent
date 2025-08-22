from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph

class AgentsMemory:
    def __init__(self, agent_name:str) -> None:
        self.agent_name = agent_name
        self.memory = self.agents_share_memory()
    def agents_share_memory(self) -> MemorySaver:
        return MemorySaver()
class ConversationMemory:
    def __init__(self) -> None:
        self.history = []
    def add(self, role, content):
        self.history.append({"role":role, "content":content})
    def get_history(self):
        return "\n".join([f"{h['role']}: {h['content']}" for h in self.history])
    