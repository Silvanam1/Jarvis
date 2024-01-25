import pyttsx3
from decouple import Config, config

from datetime import datetime

import speech_recognition as sr
from random import choice



# def speak(text):
#     """Usado para decir cualquier texto que le sea entregado"""
#
#     engine.say(text)
#     engine.runAndWait()

#
# def greet_user():
#     """Saluda al usuario de acuerdo al horario"""
#
#     hour = datetime.now().hour
#     if (hour >= 6) and (hour < 12):
#         pyttsx3.speak(f"Buenos días {USERNAME}")
#     elif (hour >= 12) and (hour < 16):
#         pyttsx3.speak(f"Buenas tardes {USERNAME}")
#     elif (hour >= 16) and (hour < 19):
#         pyttsx3.speak(f"Buenas noches {USERNAME}")
#     pyttsx3.speak(f"Yo soy JARVIS. ¿Cómo puedo asistirle?")


def take_user_input():
    """Toma las entradas del usuario, las reconoce utilizando el módulo de reconocimiento de voz y lo transforma a texto"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconociendo...')
        query = r.recognize_google(audio, language='es-es')
        if not 'Salir' in query or 'Alto' in query:
            pyttsx3.speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                pyttsx3.speak("Buenas noches señor, !cuídese!")
            else:
                pyttsx3.speak('¡Tenga un buen día señor!')
            exit()
    except Exception:
        pyttsx3.speak('Disculpe, no he podido entender. ¿Podría decirlo de nuevo?')
        query = 'None'
    return query

# import speech_recognition as sr
# import pyttsx3
# from datetime import datetime
#
#
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Di algo:")
#         audio = recognizer.listen(source)
#
#     try:
#         command = recognizer.recognize_google(audio)
#         print("Comando reconocido: " + command)
#         return command.lower()
#     except sr.UnknownValueError:
#         print("No se pudo entender el audio")
#         return ""
#     except sr.RequestError as e:
#         print(f"Error en la solicitud a Google: {e}")
#         return ""
#
#
# def execute_command(command):
#     if "open" in command:
#         # Lógica para abrir una aplicación
#         print("Abriendo la aplicación...")
#     elif "search" in command:
#         # Lógica para buscar en la web
#         print("Buscando en la web...")
#     else:
#         print("Comando no reconocido")
#
#
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
#
# speak("Hola, soy Jarvis. ¿En qué puedo ayudarte?")
#
# while True:
#     command = recognize_speech()
#     execute_command(command)
