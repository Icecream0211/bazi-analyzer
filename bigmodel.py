from ai_models.factory import AIModelFactory
from ai_models.chat import chat_with_ai

def main():
    glm4_api_key = "YOUR_GLM4_API_KEY"  # 替换为您的GLM-4 API密钥
    claude_api_key = "YOUR_CLAUDE_API_KEY"  # 替换为您的Claude API密钥
    chatgpt_api_key = "YOUR_CHATGPT_API_KEY"  # 替换为您的ChatGPT API密钥

    print("请选择要使用的模型:")
    print("1. GLM-4")
    print("2. Claude")
    print("3. ChatGPT")
    choice = input("请输入选项编号: ")

    if choice == "1":
        model_name = "glm-4"
        api_key = glm4_api_key
    elif choice == "2":
        model_name = "claude"
        api_key = claude_api_key
    elif choice == "3":
        model_name = "chatgpt"
        api_key = chatgpt_api_key
    else:
        print("无效的选择，程序退出。")
        return

    try:
        ai_model = AIModelFactory.get_model(model_name, api_key)
        
        while True:
            user_input = input("请输入您的问题 (输入'退出'结束对话): ")
            if user_input.lower() == '退出':
                print("谢谢使用,再见!")
                break
            
            response = chat_with_ai(ai_model, user_input)
            print(f"{model_name.upper()}:", response)
            print()
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
