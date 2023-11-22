from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai  # 需要安装 openai 库
from gtts import gTTS  # 需要安装 gtts 库

openai.api_key = 'YOUR_OPENAI_API_KEY'  # 请替换为你的 OpenAI API 密钥

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # 调用 ChatGPT 获取回答
        chatgpt_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=150
        ).choices[0].text.strip()
        
        # 保存对话历史
        Conversation.objects.create(user_input=user_input, chatgpt_response=chatgpt_response)
        
        # 将回答转换为语音
        tts = gTTS(chatgpt_response, lang='en')
        tts.save('freetalk/static/freetalk/audio/response.mp3')
        
        return JsonResponse({'response': chatgpt_response})
    else:
        conversations = Conversation.objects.all()
        return render(request, 'freetalk/chat.html', {'conversations': conversations})
