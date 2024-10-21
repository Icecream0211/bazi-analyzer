import openai
from .base import AIModel

class ChatGPTModel(AIModel):
    def __init__(self, api_key):
        openai.api_key = api_key

    def chat(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"发生错误: {str(e)}"
