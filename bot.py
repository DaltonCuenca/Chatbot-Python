import tkinter as tk
from tkinter import scrolledtext
import re
import random
import json
import time
from datetime import datetime

# Cargar los patrones y respuestas desde el archivo JSON
with open("patrones-respuestas.json", encoding="utf-8") as file:
    patterns = json.load(file)

# Crear un diccionario de patrones y respuestas
patterns_dict = {}
for intent, data in patterns.items():
    patterns_dict[intent] = [
        (re.compile(item["pattern"], re.IGNORECASE), item["response"]) for item in data]

# Definir la función para procesar la entrada del usuario


def process_input(user_input, patterns_dict, chatlog):
    for intent, patterns in patterns_dict.items():
        for pattern, responses in patterns:
            if pattern.search(user_input):
                response = random.choice(responses)
                response = formateo_variables(response)
                chatlog.config(state=tk.NORMAL, wrap="word")
                chatlog.insert(tk.END, "Bot: " + response + "\n\n")
                chatlog.config(state=tk.DISABLED)
                chatlog.see(tk.END)
                return response


def formateo_variables(respuesta):
    hora_actual = datetime.now().time()
    hora_formateada = hora_actual.strftime("%H:%M:%S")
    respuesta_formateada = respuesta.replace("[hora]", hora_formateada)
    return respuesta_formateada

# Definir la función para enviar la entrada del usuario


def send_input(event=None):
    user_input = input_box.get()
    chatlog.config(state=tk.NORMAL, wrap="word")
    chatlog.insert(tk.END, "Usuario: " + user_input + "\n\n")
    chatlog.config(state=tk.DISABLED)
    chatlog.see(tk.END)
    input_box.delete(0, tk.END)
    process_input(user_input, patterns_dict, chatlog)

# Crear la ventana principal
root = tk.Tk()
root.title("Chatbot")

# Crear un widget de diálogo enriquecido
chatlog = scrolledtext.ScrolledText(root, width=50, height=15)
chatlog.configure(state='disabled')

# Crear un cuadro de entrada de texto
input_box = tk.Entry(root, width=90, highlightthickness=20,
                     highlightcolor="#252526")
input_box.bind("<Return>", send_input)

# Colocar los widgets en la ventana principal
chatlog.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
input_box.pack(side=tk.BOTTOM, fill=tk.X)

# Iniciar el bucle principal de la ventana
root.mainloop()