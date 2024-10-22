from zhipuai import ZhipuAI
from .base import AIModel

class GLM4Model(AIModel):
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)

    def chat(self, prompt, systemPrompt):
        try:
            response = self.client.chat.completions.create(
                model="glm-4",
                messages=[
                    {"role": "user", "content": prompt},
                    {"role": "system", "content": systemPrompt}
                ],
                temperature=0.4,
                top_p=0.7,
                do_sample=True,
                max_tokens=4096
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"发生错误: {str(e)}"

    def stream_chat(self, prompt, systemPrompt):
        try:
            response = self.client.chat.completions.create(
                model="glm-4",
                messages=[
                    {"role": "user", "content": prompt},
                    {"role": "system", "content": systemPrompt}
                ],
                temperature=0.4,
                top_p=0.7,
                do_sample=True,
                max_tokens=4096,
                stream=True  # 启用流式响应
            )
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"发生错误: {str(e)}"
