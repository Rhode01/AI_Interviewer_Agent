class ConversationMemory:
    def __init__(self) -> None:
        self.history = []
    def add(self, role, content):
        self.history.append({"role":role, "content":content})
    def get_history(self):
        return "\n".join([f"{h['role']}: {h['content']}" for h in self.history])
    