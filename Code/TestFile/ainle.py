from openai import OpenAI

client = OpenAI(
    api_key="sk-fbf83478aced465f99583f3e520f1a8b",  # 替换成真实DashScope的API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务endpoint
)
completion = client.chat.completions.create(
    model="qwen-turbo",
    messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
              {'role': 'user', 'content': '如何做炒西红柿鸡蛋？'}],
    stream=True
)
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")