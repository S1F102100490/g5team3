# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from gtts import gTTS
import os

@csrf_exempt
def chatgpt(request):
    openai.api_key = "SPhexIGEF2VCHEkiBC1RnIhCmQb97438jbyBK0D-F84N7U_NCE8Iy0O40aPLg7RBSWKhIccjb_rbwqb82lSf1_Q"
    openai.api_base = "https://api.openai.iniad.org/api/v1"

    # Initialize or get the chat history from the session
    chat_history = request.session.get('chat_history', [])

    # Check if the 'clear_history' parameter is present in the URL
    if request.GET.get('clear_history') == 'true':
        # Clear the chat history
        
        request.session['chat_history'] = []
        media_path = "./freetalk/static/media"
        for file_name in os.listdir(media_path):
            if file_name.endswith(".mp3"):
                file_path = os.path.join(media_path, file_name)
                os.remove(file_path)
        return redirect('chatgpt')

    if request.method == 'POST':
        question = request.POST.get('question', '')

        # Add user's question to the chat history
        chat_history.append({"role": "user", "content": question})
        messages_for_gpt = [ {"role": message["role"], "content": message["content"]}
        for message in chat_history]
       # ChatGPT interaction
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an English teacher for beginners. Respond in clear and simple English ant  bewteen 20 and 40 words."},
                *messages_for_gpt  # Include the chat history in the messages
            ]
        )

        answer = response['choices'][0]['message']['content']

        # Check if the answer is too long
        answer_too_long = len(answer) > 300  # Adjust the threshold as needed

        # Convert ChatGPT's answer to speech
        speech_file_path = os.path.join("./freetalk/static/media/", f"speech_{len(chat_history)}.mp3")
        tts = gTTS(answer, lang='en')
        tts.save(speech_file_path)
        
        # Add ChatGPT's answer and speech file path to the chat history
        chat_history.append({"role": "assistant", "content": answer, "id": int(len(chat_history)/2), 'path': f'/static/media/speech_{len(chat_history)}.mp3'  })

        # Update the chat history in the session
        request.session['chat_history'] = chat_history

        # Pass the chat history to the template
        return render(request, 'freetalk/chat.html', {'question': question, 'answer': answer, 'chat_history': chat_history })

    return render(request, 'freetalk/chat.html', {'chat_history': chat_history})

def chat_view(request):
    return render(request, 'freetalk/chat.html')


