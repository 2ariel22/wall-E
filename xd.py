import speech_recognition as sr
import keyboard,serial

r = sr.Recognizer()
mic = sr.Microphone()

is_listening = False
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


keyboard.add_hotkey('k', toggle_listening)
print("Presiona la tecla 'k' para comenzar a escuchar...")
keyboard.wait()
