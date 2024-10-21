from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json

glm4_model = GLM4Model("c071cdc6b53eb53e1cd1cd6ad0a5e4db.fEV7OrCxYmiqazjd")


## 感情
def bazi_love_ai_analysis(result):
    prompt = f"""
    八字信息:{result['bazi']},
    大运信息:{result['da_yun']},
    调侯信息:{result['tiao_hou']}{result['jin_bu_huan']}{result['ge_ju']},
    八字冷暖:{result['temp_scores']},
    八字五行分数喜忌:{result['wuxing_scores']}{result['gan_scores']}{result['strong_weak_score']}

    """
    systemPrompt = """
    你是一位资深的八字分析专家，请按照以下三部分内容进行详尽分析，并注意语言风格要通俗易懂，每部分控制在 100 字以内：
    1.用户八字特征及五行平衡：概述八字中五行（金木水火土）的分布和强弱情况，分析天干地支的相生相克关系，指出这种五行格局对用户性格、情感和行为的影响。
    2.未来三年的运势预测：结合大运和流年，预测未来三年在事业、财运、健康等方面的整体运势走势，列举可能出现的转折点、挑战或机遇。
    3.对用户的个人建议：基于前两部分分析结果，提出在生活、职业、感情方面的具体行动建议，帮助用户趋吉避凶。
    4.输出参考："八字特征及五行平衡：此八字水旺土厚，金木相对平衡，火稍弱。天干地支中，水能生木，土能生金，形成相生关系；但同时水克火，火被抑制。这样的五行格局造就了用户坚韧、冷静的性格，但有时可能过于保守，缺乏激情。在情感上，可能不太善于表达，行为上则可能过于谨慎。未来三年的运势预测：未来三年，结合大运和流年，整体运势平稳中带波动。事业上有上升空间，但需注意决策，避免因保守错失良机。财运方面，投资需谨慎，尤其避免第三季度的高风险项目。健康方面，注意调养，尤其是冬季。2023年是一个转折点，可能会有新的机遇出现。
    对用户的个人建议：在生活上，建议多参与社交活动，增强人际交往能力。职业上，若遇到瓶颈，可在2023年考虑新的发展方向。感情方面，应主动表达情感，避免错过良缘。注意，未来一年中，若事业发展受阻，可在第三季度尝试新的策略，灵活调整，以利转运"。
    """
    print(prompt)
    print()
    print(systemPrompt)
    print('-'*100)
    interpreted_result = glm4_model.chat(prompt,systemPrompt)
    return interpreted_result