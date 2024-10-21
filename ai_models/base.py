from abc import ABC, abstractmethod

class AIModel(ABC):
    @abstractmethod
    def chat(self, prompt):
        pass
