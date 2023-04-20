# De documento
import re
import random
import json
import time

# De variables
from datetime import datetime

# JSON es un formato de texto ligero que se utiliza para intercambiar datos. 
# Es fácil de leer y escribir para los seres humanos y fácil de analizar 
# y generar para las máquinas.
# El archivo json en este caso contiene patrones y respuestas que las
# usaremos para responder al usuario

# with open abre el archivo con codificacion utf-8, guarda el archivo dentro
# de la variable patterns, with open cierra el archivo despues de ser usado.
with open("patrones-respuestas.json", encoding="utf-8") as file:
    patterns = json.load(file)

# Crear un diccionario de patrones y respuestas
patterns_dict = {}
# Llenamos el diccionario con la informacion de la variable patterns
for indice, data in patterns.items():
    patterns_dict[indice] = [
        (re.compile(item["pattern"], re.IGNORECASE), item["response"]) for item in data]

# Definir la función para procesar la entrada del usuario
def process_input(user_input, patterns_dict):
    # separamos los patrones en items
    for indice, patterns in patterns_dict.items():
        # separamos los items en patron y respuesta
        for pattern, responses in patterns:
            # buscamos si un patron es similar a lo que el usuario
            # escribio
            if pattern.search(user_input):
                # Damos una respuesta aleatoria a la pregunta
                response = random.choice(responses)
                #Formateamos variables si se requiere
                response = formateo_variables(response)
                #cada caracter de la respuesta se presenta cada 0.02 segundos
                for char in response:
                    print(char, end='', flush=True)
                    time.sleep(0.02)
                print('\n')


def formateo_variables(respuesta):
    
    hora_actual = datetime.now().time()
    hora_formateada = hora_actual.strftime("%H:%M:%S")
    respuesta_formateada = respuesta.replace("[hora]", hora_formateada)
    return respuesta_formateada


# Bucle de chat
while True:
    # Pedimos informacion al usuario
    input_text = input("> ")
    #si la informacion esta vacia
    if not input_text:
        #repetimos el ciclo
        continue
    # de lo contrario
    else:
        # Si lo que el usuario escribio es adios o salir
        if input_text.lower() in ["adios", "salir"]:
            #cierra el programa
            exit()
        #de lo contrario llama a la funcion process input
        process_input(input_text, patterns_dict)