from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json

glm4_model = GLM4Model("c071cdc6b53eb53e1cd1cd6ad0a5e4db.fEV7OrCxYmiqazjd")


## 事业
def bazi_career_ai_analysis(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    
    你是一位精通八字命理的职业规划专家，请根据以下用户的八字信息，从职业发展的角度提供具体建议。请从以下几个方面进行分析，并提供可操作的职业方向建议：
    职业方向选择：根据五行平衡和用户性格特点，推荐适合的职业方向（例如：教育、管理、技术等）。
    适合行业：指出最适合用户的行业，并解释该行业与其八字命局之间的关系。
    职业发展策略：提出未来三年内的职业发展策略，例如：‘如果未来两年事业运较差，可考虑在这一年多学习提升，避免冒进’。
    """

    systemPrompt = """
    你是一位专业的八字分析师。请基于给定的八字信息进行分析，直接给出洞察和建议。
    避免重复原始数据，专注于提供有价值的解读和建议。
    使用通俗易懂的语言，确保分析结果清晰、简洁且富有洞察力。
    """
    print(prompt)
    print()
    print(systemPrompt)
    print('-'*100)
    interpreted_result = glm4_model.chat(prompt,systemPrompt)
    return interpreted_result