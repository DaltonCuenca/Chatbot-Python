
#django
import os
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

# De documento
import re
import random
import json
import time

# De variables
from datetime import datetime

with open(os.path.join(os.path.dirname(__file__), 'data', 'patrones-respuestas.json'), encoding="utf-8") as file:
    patterns = json.load(file)

# Crear un diccionario de patrones y respuestas
patterns_dict = {}
for indice, data in patterns.items():
    patterns_dict[indice] = [
        (re.compile(item["pattern"], re.IGNORECASE), item["response"]) for item in data]

# Definir la función para procesar la entrada del usuario
def process_input(user_input, patterns_dict):
    for indice, patterns in patterns_dict.items():
        for pattern, responses in patterns:
            if pattern.search(user_input):
                response = random.choice(responses)
                response = formateo_variables(response)
                return {"response": response}


def formateo_variables(respuesta):
    
    hora_actual = datetime.now().time()
    hora_formateada = hora_actual.strftime("%H:%M:%S")
    respuesta_formateada = respuesta.replace("[hora]", hora_formateada)
    return respuesta_formateada


# @csrf_exempt
def chatbot(request):
    # Inicializa el historial de conversación de la sesión o recupera el historial de conversación actual si existe
    conversation = request.session.get('conversation', [])
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()
        if user_input:
            bot_response = process_input(user_input, patterns_dict)
            conversation.append({'pregunta': user_input, 'respuesta': bot_response})

    # Guarda el historial de conversación en la sesión
    request.session['conversation'] = conversation

    context = {'obj': conversation}
    return render(request, 'chat/index.html', context)

def borrar_conversacion(request):
    # Elimina el historial de conversación de la sesión
    del request.session['conversation']
    return redirect('chat/index.html')