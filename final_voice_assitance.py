# Asistente de voz (Jarvis)
# import - anade paquetes a el marco de trabajo
import datetime
# cuando usamos import <nombre del paquete> as <apodo>
import speech_recognition as sr
import pyttsx3 as py2text
import wikipedia
import pywhatkit as pw
import random
import pywhatkit
from translate import Translator


__author__ = 'Julio Martinez'
__date__ = datetime.time

# lista de contactos
contactos = {
    'carlos': '+529711855338',
    'abel': '+529513610976'
}

# -------------------------------------------------------------------------------------------------------------
# Hacer que nuestro asistente de voz--- hable
bocinas = py2text.init()
voces = bocinas.getProperty('voices')
bocinas.setProperty('voice', voces[2].id)
bocinas.setProperty('rate', 160)
# Hace que las bocinas hablen
bocinas.say("Hola soy alexa")
bocinas.say("En que te puedo ayudar?")
# Ejecuta lo que queremos que digan las bocinas
bocinas.runAndWait()
listener = sr.Recognizer()


# ------------- Escuchar -----------------
def listen_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Escuchando .....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='es-US')
            command = command.lower()
            print(command)
    except:
        pass
    return command


# comnado va a ser el nombre de la variable que escucho
# -----------------------------------------------------------------------
comando = listen_command()
# -----------------------------------------------------------------------
print(comando)
# Evaluar si Jarvis esta en la oracion:

if 'alexa' in comando or 'alexis' in comando:
    # Si Jarvis esta en la Oracion, vamos a continuar con la instruccion
    if 'hora' in comando:
        # preguntar el tiempo a la computadora
        tiempo_actual = datetime.datetime.now().strftime('%H:%M')
        bocinas.say('La hora actual es ' + tiempo_actual)
        bocinas.runAndWait()
    # elif -- else if -- maneja la respuesta falsa de la pregunta anterior y hace una nueva pregunta
    elif 'busca' in comando:
        comando = comando.replace('alexa', '')
        comando = comando.replace('alexis', '')
        comando = comando.replace('busca', '')
        # buscamos el comando sin Alexa y sin la instruccion search
        try:
            p = wikipedia.page(comando)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            p = wikipedia.page(s)
        #wiki_search = wikipedia.summary(comando, sentences = 0 , chars = 0 , auto_suggest = True , redirect = True )
        wiki_search = p.summary
        translator = Translator(to_lang="Spanish")
        translation = translator.translate(wiki_search)
        bocinas.say(translation)
        bocinas.runAndWait()
    elif 'reproduce' in comando:
        comando = comando.replace('alexa', '')
        comando = comando.replace('alexis', '')
        comando = comando.replace('reproduce', '')
        bocinas.say("Reproduciendo " + comando)
        bocinas.runAndWait()
        pw.playonyt(comando);
    elif 'envia' in comando or 'whatsapp' in comando or 'envía' in comando:
        bocinas.say('A quien le quieres enviar un whatsapp?')
        bocinas.runAndWait()
        nombre = listen_command()
        #nombre = 'carlos'
        if nombre in contactos.keys():
            cel = contactos.get(nombre)
            bocinas.say("Cual es el mensaje?")
            bocinas.runAndWait()
            mensaje = listen_command()
            hora = datetime.datetime.now().strftime('%HH:%MM')
            h, m = hora.split(':')
            h = int(h[:-1])
            m = int(m[:-1])
            pywhatkit.sendwhatmsg(cel, mensaje, h, m+1)

    else:
        print('No puedo hacer la accion que pides')


else:
    print('No me estas hablando')
