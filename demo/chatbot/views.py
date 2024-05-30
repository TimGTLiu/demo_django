from django.shortcuts import render
from django.http import JsonResponse
# from .langchain_client.py import get_langchain_response


def chat_view(request):
    return render(request, 'chatbot/chat.html')


def get_response(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        message = data.get('message', '')
        response = "I'm a cool chatbot"
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
