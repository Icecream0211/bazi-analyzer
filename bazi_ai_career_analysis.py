from ai_models.glm4 import GLM4Model
from bazi_need import get_bazi_need
import json

glm4_model = GLM4Model("754e9e67eb184a108e6df79c473edeae.PQehlQintzJUHPVb")

def bazi_career_ai_analysis(result):
    prompt_format = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    """

    prompt = """
    请根据用户的命局、大运、喜用神和忌用神等，详细分析用户的事业运势，并按以下格式输出结果：

    1. 职业方向选择（200字以内）：
    根据用户的八字特点，分析最适合的职业方向。考虑五行平衡、用户性格特点等因素，给出3-5个具体的职业建议。

    2. 最适合的职业和行业（JSON格式）：
    请输出一个JSON数组，包含用户最适合的职业及其匹配度（满分10分）。例如：    ```json
    [
      {"职业": "教育培训", "匹配度": 9},
      {"职业": "管理与领导", "匹配度": 8},
      {"职业": "技术与工程", "匹配度": 7},
      {"职业": "财务与投资", "匹配度": 6},
      {"职业": "创意行业", "匹配度": 7}
    ]    ```

    3. 适合行业（100字以内）：
    列出2-3个最适合用户的行业，并简要解释原因。

    4. 职业发展策略（200字以内）：
    结合大运和流年，分析未来五年的事业发展策略。包括关键年份、可能的机遇和挑战，以及应对建议。

    5. 具体建议（150字以内）：
    提供3-5条具体的职业发展建议，包括如何提升能力、避开风险等。

    请确保分析结果具体、实用，并直接与用户的八字特征相关联。避免笼统或模糊的表述，给出清晰、可操作的指导。
    """

    system_prompt = """
    你是一位专业的八字分析师，专攻事业和职业发展分析。请基于给定的八字信息进行分析，直接给出洞察和建议。
    避免重复原始数据，专注于提供有价值的解读和建议。
    使用通俗易懂的语言，确保分析结果清晰、简洁且富有洞察力。
    严格按照要求的格式输出结果，特别注意JSON格式的正确性。
    """

    print(prompt)
    print()
    print(system_prompt)
    print('-'*100)
    interpreted_result = glm4_model.chat(prompt_format+prompt, system_prompt)
    return interpreted_result




def bazi_career_ai_analysis_stream(result):
    prompt_format = f"""
    基于以下八字信息进行分析：
    {json.dumps(result, ensure_ascii=False)}
    """

    prompt = """
    请根据以下用户的八字信息，从职业发展的角度提供具体建议。请从以下几个方面进行分析，并提供可操作的职业方向建议：
    职业方向选择：根据五行平衡和用户性格特点，推荐适合的职业方向（例如：教育、管理、技术等）。
    适合行业：指出最适合用户的行业，并解释该行业与其八字命局之间的关系。
    职业发展策略：提出未来三年内的职业发展策略，例如：‘如果未来两年事业运较差，可考虑在这一年多学习提升，避免冒进’。
    """

    system_prompt = """
    你是一位精通八字命理的职业规划专家,请基于给定的八字信息进行分析，直接给出洞察和建议。
    避免重复原始数据，专注于提供有价值的解读和建议。
    """

    print(prompt)
    print()
    print(system_prompt)
    print('-'*100)
    for chunk in glm4_model.stream_chat(prompt_format+prompt, system_prompt):
        yield chunk
