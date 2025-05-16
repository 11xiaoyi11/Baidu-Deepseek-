import os
from openai import OpenAI

def generate_answer(prompt):
    """
    生成回答
    :param prompt: 提供给模型的 Prompt
    :return: 模型的回答
    """
    # 使用 OpenAI API
    client = OpenAI(
        api_key= "API_KEY", # 在这里将 API_KEY 替换为你从开放平台申请的 API Key
        base_url="https://api.lkeap.cloud.tencent.com/v1/chat/completions",
    )

    # 调用模型
    completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=[
        {'role': 'user', 'content': prompt}
        ],
        temperature=0.3,
    )
    
    return completion.choices[0].message.content


def generate_prompt(template_path, user_question, results_list):
    """
    生成用于模型的 Prompt
    :param template_path: 模板文件路径
    :param user_question: 用户提问
    :param results_list: 搜索结果列表
    :return: 格式化后的 Prompt
    """
    # 拼接百度搜索摘要
    formatted_results = ""
    for i, result in enumerate(results_list, 1):
        title = result.get('title', '无标题')
        summary = result.get('summary', '无摘要')
        formatted_results += f"{i}. 标题：{title}\n 摘要：{summary}\n\n"

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"模板文件 {template_path} 不存在。")
    
    # 读取模板文件
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # 构建完整 prompt
    prompt = template.format(
        user_question=user_question,
        results_list=formatted_results
    )
    return prompt
