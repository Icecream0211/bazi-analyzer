from zhipuai import ZhipuAI
from .base import AIModel

class GLM4Model(AIModel):
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)

    def chat(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="glm-4",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"发生错误: {str(e)}"
