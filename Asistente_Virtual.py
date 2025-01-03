import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz/idioma
id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# escuchar microfono y devolver el audio como texto
def tranformar_audio_en_texto():

    # alamacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabación
        print('ya puedes hablar')

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver a pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print("ups, no entendí")

            # devolver error
            return "sigo esperando"

        # en caso de no poder resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendió el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendió el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


# funcion para el que asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el día de la semana
def pedir_dia():

    # crear varibale con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear una variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombre de los dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domimgo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():

    # crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)


# funcion saludo inicial
def saludo_inicial():

    # cear variabales con datos hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    # decir saludo
    hablar(f'{momento}, soy Rebeca, tu asistente personal. Por favor dime en que te puedo ayudar')


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el microfono y guardar el pedido en un string
        pedido = tranformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Un gusto, voy a abrir YouTube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro espera un momento')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abre mi curso' in pedido:
            hablar('Por supuesto')
            webbrowser.open('https://www.udemy.com/course/python-total/learn/lecture/29685030#overview')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Por supuesto, dame un segundo en lo que lo encuentro')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproduce' in pedido:
            hablar('Buena idea, ahorita mismo lo hago')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'Amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La he encontrado, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón no la pude encontrar')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa házmelo saber')
            break
        elif 'abre whatsapp' in pedido:
            hablar('En un momento abro tus mensajes')
            pywhatkit.open_web()
            continue
        elif 'muchas gracias' in pedido:
            hablar('Es un gusto poder ayudar. Para apagarme di la palabra adiós')
            continue
        elif 'toma una captura de pantalla' in pedido:
            hablar('Aguarda un momento')
            pywhatkit.take_screenshot(pedido)
            continue


pedir_cosas()
