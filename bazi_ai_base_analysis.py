from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json
import os

glm4_model = GLM4Model("754e9e67eb184a108e6df79c473edeae.PQehlQintzJUHPVb")


## 基础八字分析
def bazi_base_ai_analysis(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    
    请直接给出分析结果，不要重复输入的信息。分析应包括以下三个方面，每个部分控制在200字以内：
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


def bazi_base_ai_analysis_stream(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    
    请按照以下三部分内容进行详尽分析，并注意语言风格要通俗易懂，每部分控制在 100 字以内：
    八字特征及五行平衡：概述八字中五行（金木水火土）的分布和强弱情况，分析天干地支的相生相克关系，指出这种五行格局对用户性格、情感和行为的影响。
    未来三年的运势预测：结合大运和流年，预测从2024年开始未来三年在事业、财运、健康等方面的整体运势走势，列举可能出现的转折点、挑战或机遇。
    对用户的个人建议：基于前两部分分析结果，提出在生活、职业、感情方面的具体行动建议，帮助用户趋吉避凶。例如：‘若未来一年事业发展受阻，可考虑在第三季度变更策略。’
    """
    system_prompt = """
    你是一位精通八字命理的分析师，现在请根据用户的八字信息进行整体的八字分析。
    """
    
    for chunk in glm4_model.stream_chat(prompt, system_prompt):
        print(chunk)
        yield chunk
