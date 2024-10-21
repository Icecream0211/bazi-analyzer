from .glm4 import GLM4Model
from .claude import ClaudeModel
from .chatgpt import ChatGPTModel

class AIModelFactory:
    @staticmethod
    def get_model(model_name, api_key):
        if model_name.lower() == "glm-4":
            return GLM4Model(api_key)
        elif model_name.lower() == "claude":
            return ClaudeModel(api_key)
        elif model_name.lower() == "chatgpt":
            return ChatGPTModel(api_key)
        else:
            raise ValueError(f"不支持的模型: {model_name}")
