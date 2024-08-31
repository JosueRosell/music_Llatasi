import time
import speech_recognition as sr

# Función para mostrar la letra como si estuviera escribiéndose en tiempo real
def escribir_letra(letra, velocidad=0.1):
    for char in letra:
        print(char, end='', flush=True)
        time.sleep(velocidad)  # Pausa entre cada carácter

# Función para reconocer el habla
def reconocer_habla():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Por favor, habla ahora...")
        audio = recognizer.listen(source)
        try:
            # Convertir audio en texto
            texto = recognizer.recognize_google(audio, language="es-ES")
            print("\nTexto reconocido: " + texto)
            return texto
        except sr.UnknownValueError:
            print("Lo siento, no pude entender lo que dijiste.")
        except sr.RequestError as e:
            print("Error con el servicio de reconocimiento de voz; {0}".format(e))
        return ""

# Capturar y escribir el texto del micrófono
texto_escuchado = reconocer_habla()
if texto_escuchado:
    escribir_letra(texto_escuchado, velocidad=0.05)
