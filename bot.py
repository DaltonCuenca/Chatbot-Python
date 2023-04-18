# De documento
import re
import random
import json
import time

# De variables
from datetime import datetime

with open("patrones-respuestas.json", encoding="utf-8") as file:
    patterns = json.load(file)

# Crear un diccionario de patrones y respuestas
patterns_dict = {}
for intent, data in patterns.items():
    patterns_dict[intent] = [
        (re.compile(item["pattern"], re.IGNORECASE), item["response"]) for item in data]

# Definir la función para procesar la entrada del usuario
"""
    Toma una entrada del usuario y un diccionario de patrones y respuestas, y devuelve una respuesta
    aleatoria del diccionario si la entrada del usuario coincide con alguno de los patrones.
    
    :param user_input: La entrada del usuario, que suponemos que se ha procesado previamente antes de
    pasar al bot
    :param patterns_dict: un diccionario de diccionarios. Las claves son los nombres de las intenciones
    y los valores son diccionarios que contienen los patrones y las respuestas para esa intención
    :return: Una respuesta aleatoria de la lista de respuestas.
    Ejemplo de respuestas por defecto:
    {
        "otro": [
            {
                "pattern": "",
                "response": [
                    "Lo siento, no entiendo la pregunta. ¿Podrías preguntar de otra manera?",
                    "No estoy seguro de entender lo que preguntas. ¿Podrías reformular tu pregunta?"
                ]
            }
        ]
    }
"""
def process_input(user_input, patterns_dict):
    for intent, patterns in patterns_dict.items():
        for pattern, responses in patterns:
            if pattern.search(user_input):
                response = random.choice(responses)
                response = formateo_variables(response)
                # # Definir el ancho máximo de línea
                # line_width = 80
                # # Envolver el texto en líneas de ancho máximo
                # response = textwrap.fill(response, width=line_width)
                for char in response:
                    print(char, end='', flush=True)
                    time.sleep(0.02)
                print('\n')
                return response


def formateo_variables(respuesta):
    
    hora_actual = datetime.now().time()
    hora_formateada = hora_actual.strftime("%H:%M:%S")
    respuesta_formateada = respuesta.replace("[hora]", hora_formateada)
    return respuesta_formateada


# Bucle de chat
while True:
    # Obtener la entrada del usuario
    input_text = input("> ")
    if not input_text:
        continue
    else:
        if input_text.lower() in ["adios", "salir"]:
            exit()
        output_text = process_input(input_text, patterns_dict)