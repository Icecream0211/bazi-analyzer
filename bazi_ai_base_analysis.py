from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json

glm4_model = GLM4Model("c071cdc6b53eb53e1cd1cd6ad0a5e4db.fEV7OrCxYmiqazjd")


## 基础八字分析
def bazi_base_ai_analysis(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    
    请直接给出分析结果，不要重复输入的信息。分析应包括以下三个方面，每个部分控制在100字以内：
    1. 八字特征及五行平衡
    2. 未来三年的运势预测
    3. 对用户的个人建议
    """

    system_prompt = """
    你是一位专业的八字分析师。请基于给定的八字信息进行分析，直接给出洞察和建议。
    避免重复原始数据，专注于提供有价值的解读和建议。
    使用通俗易懂的语言，确保分析结果清晰、简洁且富有洞察力。
    """

    print(prompt)
    print()
    print(system_prompt)
    print('-'*100)
    interpreted_result = glm4_model.chat(prompt,system_prompt)
    return interpreted_result
