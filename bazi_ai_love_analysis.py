from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json

glm4_model = GLM4Model("c071cdc6b53eb53e1cd1cd6ad0a5e4db.fEV7OrCxYmiqazjd")


## 感情
def bazi_love_ai_analysis(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    你是一位擅长情感分析的八字命理专家，用户提供了以下八字信息。请根据用户的八字，详细分析其感情运势，并围绕以下几方面展开解读：
    感情性格特征：基于八字中五行的平衡情况和日主的强弱特征，分析用户在感情中的性格表现（如：是否主动、是否重情重义、对待感情的态度等）。
    感情发展趋势：结合大运和流年，预测未来三年内用户的感情发展走势。描述可能出现的情感转折点、婚姻运势、或者感情中的挑战和机遇。
    择偶建议：根据用户八字中的喜用神和情感需求，提供理想伴侣的五行特征、性格类型和适合的交往方式，并分析如何提升感情运势（如：如何调整心态，避免某些情感误区等）。
    重要时机提醒：指出未来三年中适合发展感情或结婚的具体年份和月份，并说明如何利用这些时机推动感情生活。
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