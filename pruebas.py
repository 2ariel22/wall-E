import speech_recognition as sr
import keyboard,serial,pyttsx3


r = sr.Recognizer()
mic = sr.Microphone()

is_listening = False

def hablar(texto):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # Establece la voz en español latinoamericano
    engine.setProperty('rate', 150)  # Ajusta la velocidad de la voz a 150 palabras por minuto
    engine.setProperty('volume', 1.0)  # Establece el volumen en 1.0 (máximo)
    engine.setProperty('pitch', 50)  # Ajusta el tono de la voz a 50 (más bajo)
    engine.say(texto)  # Mensaje a reproducir
    engine.runAndWait()  # Reproduce el mensaje de voz

def ola(u):
        if("guayaba" in u):
            hablar("imprimiendo wuayaba en el lcd")
            ser.write(b'1')
        elif("guanábana" in u):
            hablar("imprimiendo wuanabana en el lcd")
            ser.write(b'2')
        elif("temperatura" in u):
            hablar("analizando datos de temperatura y humedad")
            ser.write(b'3')
        elif("distancia" in u):
            hablar("midiendo distancia")
            ser.write(b'4')
        elif("izquierda" in u):
            hablar("girando a la izquierda")
            ser.write(b'5')
        elif("derecha" in u):
            hablar("girando a la derecha")
            ser.write(b'6')
        elif("apagar" in u):
            hablar("deteniendo ruedas")
            ser.write(b'6')
        elif("finalizar" in u):
            hablar("conexion finalizada")
            ser.close()
def toggle_listening():
    global is_listening
    if not is_listening:
        print("Comenzando a escuchar...")
        is_listening = True
        with mic as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-CO")
            print("Has dicho: " + text)
        except sr.UnknownValueError:
            print("No he podido entender lo que has dicho")
        except sr.RequestError as e:
            print("Error al conectarse al servicio de reconocimiento de voz; {0}".format(e))
        is_listening = False
    else:
        print("Deteniendo la escucha...")
        is_listening = False
    ola(text.lower())
try:
    hablar("estableciendo conexion con wally")
    ser = serial.Serial("COM4",9600)
    hablar("conexion establecida con wally")   
except:
    hablar("no se pudo establecer conexion con wally")

keyboard.add_hotkey('k', toggle_listening)
print("Presiona la tecla 'k' para comenzar a escuchar...")
keyboard.wait()
