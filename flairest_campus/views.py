from django.utils.timezone import datetime
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.core.files.storage import FileSystemStorage
import re
import json
import requests


def sber_view(request):
    sms = request.POST.get("sms", "")
    
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat:latest",
        "messages": [
        {
            "role": "user",
            "content": f"{sms}"
        }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1
    })
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer <токен>'
    }

    bot_ans = requests.request("POST", url, headers=headers, data=payload, verify=False).text
    bot_ans = json.loads(bot_ans)
    bot_ans = bot_ans['choices']
    bot_ans = bot_ans[0]['message']['content']

    url1 = "https://smartspeech.sber.ru/rest/v1/text:synthesize"

    headers1 = {
        'Content-Type': 'application/text',
        'Authorization': 'Bearer <токен>'
    }

    space = bot_ans + ' '*300 
    bot_golos = requests.request("POST", url1, headers=headers1, data=f'{space}', verify=False)

    with open('flairest_campus/static/flairest_campus/test.wav', 'wb') as f:
        f.write(bot_golos.content)
    
    return render(
        request,
        'flairest_campus/indexX.html',
        {
            'answer': bot_ans
        }
    )