from django.http import JsonResponse
from django.shortcuts import render
from .views import process_input, patterns_dict, formateo_variables, chatbot

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST['user_input'] # Obtener el texto de la pregunta del usuario del parámetro POST 'user_input'
        response = process_input(user_input, patterns_dict) # Procesar la pregunta del usuario con el chatbot
        response = formateo_variables(response) # Formatear la respuesta del chatbot
        # Devolver la respuesta como un objeto JSON
        return JsonResponse({'respuesta': response})

    # Renderizar la plantilla 'chatbot.html' con la conversación existente entre el usuario y el chatbot
    return render(request, 'chatbot.html', {'obj': chatbot.conversation})
