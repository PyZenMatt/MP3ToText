from pydub import AudioSegment
import speech_recognition as sr
import logging

# Configurazione del logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Convertire MP3 in WAV
def converti_mp3_in_wav(file_mp3):
    audio = AudioSegment.from_mp3(file_mp3)
    file_wav = file_mp3.replace(".mp3", ".wav")
    audio.export(file_wav, format="wav")
    return file_wav

# Trascrivere l'audio in testo 
def trascrivi_audio(file_wav):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_wav) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="it-IT")
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition non ha potuto comprendere l'audio"
    except sr.RequestError as e:
        return f"Impossibile richiedere risultati dal servizio Google Speech Recognition; {e}"

if __name__ == "__main__":
    # Percorso del file
    file_mp3 = r"C:\Users\matte\OneDrive\Desktop\audio.mp3"  # Utilizzando stringhe raw per evitare sequenze di escape non valide

    # Conversione da MP3 a WAV e trascrizione
    file_wav = converti_mp3_in_wav(file_mp3)
    trascrizione = trascrivi_audio(file_wav)

    # Output della trascrizione
    print("Trascrizione:\n", trascrizione)
