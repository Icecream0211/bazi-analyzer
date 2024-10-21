from anthropic import Anthropic
from .base import AIModel

class ClaudeModel(AIModel):
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def chat(self, prompt):
        try:
            response = self.client.completions.create(
                model="claude-2",
                prompt=f"\n\nHuman: {prompt}\n\nAssistant:",
                max_tokens_to_sample=300
            )
            return response.completion
        except Exception as e:
            return f"发生错误: {str(e)}"
