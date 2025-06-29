from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json

glm4_model = GLM4Model("754e9e67eb184a108e6df79c473edeae.PQehlQintzJUHPVb")


## 大运分析
def bazi_dayun_ai_analysis(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    你是一位专业的八字运势分析师，请基于用户的八字信息，分析其从出生起运后的每个大运周期（每十年一个大运）。请从以下几个方面为每个大运周期进行评分，每个评分满分为 10 分：
    事业运势评分：描述该大运周期内用户在事业上的发展趋势，并评分（如：8/10）。
    财运运势评分：分析该周期内用户在财富方面的得失，列举可能的财务机遇或风险。
    健康运势评分：根据五行喜忌分析该周期内用户健康状况，给出相应的健康评分。
    情感运势评分：评估该大运周期内用户的感情生活和家庭关系，并给出评分。
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



## 大运分析
def bazi_dayun_ai_analysis_stream(result):
    prompt = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    你是一位专业的八字运势分析师，请基于用户的八字信息，分析其从出生起运后的每个大运周期（每十年一个大运）。请从以下几个方面为每个大运周期进行评分，每个评分满分为 10 分：
    事业运势评分：描述该大运周期内用户在事业上的发展趋势，并评分（如：8/10）。
    财运运势评分：分析该周期内用户在财富方面的得失，列举可能的财务机遇或风险。
    健康运势评分：根据五行喜忌分析该周期内用户健康状况，给出相应的健康评分。
    情感运势评分：评估该大运周期内用户的感情生活和家庭关系，并给出评分。
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
    for chunk in glm4_model.stream_chat(prompt, systemPrompt):
        yield chunk
