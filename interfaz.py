from tkinter import *
import speech_recognition as sr
import keyboard,serial,pyttsx3,time

r = sr.Recognizer()
mic = sr.Microphone()

raiz = Tk()
raiz.title("raptor")
raiz.iconbitmap("Wall-E.ico")
raiz.geometry("800x450")
raiz.config(bg="gray")



#contenedores
titulo = Frame(raiz)
titulo.grid(row=1,column=1)


main = Frame(raiz)
main.grid(row=2,column=1)
main.config(bg="gray")

#funciones
def hablar(texto):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # Establece la voz en español latinoamericano
    engine.setProperty('rate', 150)  # Ajusta la velocidad de la voz a 150 palabras por minuto
    engine.setProperty('volume', 1.0)  # Establece el volumen en 1.0 (máximo)
    engine.setProperty('pitch', 50)  # Ajusta el tono de la voz a 50 (más bajo)
    engine.say(texto)  # Mensaje a reproducir
    engine.runAndWait()  

def conexion():
    global ser
    try:
        hablar("estableciendo conexion con wally")
        ser = serial.Serial("COM4",9600)
        hablar("conexion establecida con wally")   
    except:
        hablar("no se pudo establecer conexion con wally")


def decision(u):
        if("guayaba" in u)or('1' in u):
            hablar("imprimiendo wuayaba en el lcd")
            ser.write(b'1')
        elif("guanábana" in u)or('2' in u):
            hablar("imprimiendo wuanabana en el lcd")
            ser.write(b'2')
        elif("temperatura" in u)or('3' in u):
            hablar("analizando datos de temperatura y humedad")
            ser.write(b'3')
            time.sleep(0.1)
            humedad = ser.readline().decode()
            print(humedad)
            var = ser.readline().decode()
            hablar("la temperatura actual es: "+var)
            hablar("la humedad relativa es: "+humedad)
            temperatura.set(f"{var} c° - {humedad}")
            
        elif("distancia" in u)or('4' in u):
            hablar("midiendo distancia")
            ser.write(b'4')
            time.sleep(0.1)
            dist = ser.readline().decode()
            hablar("la distancia al objetivo mas cercano es: "+dist+"cm")
            distancia.set(dist +" cm")
        elif("izquierda" in u)or('5' in u):
            hablar("girando a la izquierda")
            ser.write(b'5')
        elif("derecha" in u)or('6' in u):
            hablar("girando a la derecha")
            ser.write(b'6')
        elif("apagar" in u)or('7' in  u):
            hablar("deteniendo ruedas")
            ser.write(b'7')
        elif("saluda" in u)or('8' in u):
            hablar("animacion 1 de brazos")
            ser.write(b'8')

        elif("animacion" in u)or('9' in u):
            hablar("animacion 2 de brazos")
            ser.write(b'9')    
        elif("finalizar" in u)or('a' in u):
            hablar("conexion finalizada")
            ser.close()
        elif("avanzar" in u)or('b' in u):
            hablar("avanzado")
            ser.write(b'9')   

def escuchar():
   
    print("puedes hablarme, pequeño")
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-CO")
        print("Has dicho: " + text)
        decision(text.lower())
    except sr.UnknownValueError:
        print("No he podido entender lo que has dicho")
    except sr.RequestError as e:
        print("Error al conectarse al servicio de reconocimiento de voz; {0}".format(e))
    except:
        print("error critico")   
    print("fin") 
    


texto_titulo = Label(titulo,text="control y monitoreo Wall-E",font=(28))
texto_titulo.pack()
texto_titulo.config(bg="gray")

#visualizadores
temperatura=StringVar()
distancia=StringVar()

temperatura.set("ola :3")
distancia.set("7u7")

texto_visualizador1=Label(main,text="Temperatura/humedad",bg="gray",font=(20))
texto_visualizador1.grid(row=0,column=1)
visualizador1= Entry(main,textvariable=temperatura,width=35)
visualizador1.config(background="lightblue",justify="center")
visualizador1.grid(row=1,column=1,ipadx=25,ipady=10)
temp_hume = PhotoImage(file="temperatura.png")
img_temp = Label(main, image=temp_hume)
img_temp.grid(row=2,column=1)
img_temp.config(bg="gray")

texto_visualizador2=Label(main,text="distancia",bg="gray",font=(20))
texto_visualizador2.grid(row=0,column=3)
visualizador2= Entry(main,textvariable=distancia,width=35)
visualizador2.config(background="lightblue",justify="center")
visualizador2.grid(row=1,column=3,ipadx=25,ipady=10)
radar = PhotoImage(file="radar.png")
img_radar = Label(main, image=radar)
img_radar.grid(row=2,column=3)
img_radar.config(bg="gray")

walle = PhotoImage(file="wallsaludando.png")
img_walle = Label(main, image=walle)
img_walle.grid(row=1,column=2,rowspan=2)
img_walle.config(bg="gray")



keyboard.add_hotkey('w', lambda:decision('b'))
keyboard.add_hotkey('a', lambda:decision('5'))
keyboard.add_hotkey('d', lambda:decision('6'))
keyboard.add_hotkey('s', lambda:decision('7'))
keyboard.add_hotkey('q', lambda:decision('8'))
keyboard.add_hotkey('e', lambda:decision('9'))
keyboard.add_hotkey('f', lambda:decision('a'))

#botoneria
boton_temp=Button(main,text="temperatura y humedad",command= lambda:decision('3'))
boton_temp.grid(row=3,column=1,padx=25,pady=10)



boton_escucha=Button(main,text="raptor-escucha",command=lambda:escuchar())
boton_escucha.grid(row=4,column=2,padx=75,pady=10)

boton_conexion=Button(main,text="conexion",command=lambda:conexion())
boton_conexion.grid(row=5,column=2,padx=75,pady=10)


boton_dist=Button(main,text="distancia",command=lambda:decision('4'))
boton_dist.grid(row=3,column=3,padx=25,pady=10)


raiz.mainloop()