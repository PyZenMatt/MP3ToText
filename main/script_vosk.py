import wave
import logging
from vosk import Model, KaldiRecognizer

# Logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function
def trascrivi_audio_vosk(file_wav, model_path):
    logging.info(f"Inizio trascrizione con Vosk per il file: {file_wav}")
    
    # upload model
    model = Model(model_path)
    
    # opening file
    wf = wave.open(file_wav, "rb")
    
    # Verify frequency
    if wf.getframerate() != 16000:
        logging.warning("La frequenza di campionamento non è 16 kHz, il modello potrebbe non funzionare correttamente.")
    
    # Kaldi
    recognizer = KaldiRecognizer(model, wf.getframerate())

    # Inizializing
    trascrizione = ""
    
    # read data
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break  # end of file audio
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            trascrizione += result  # Results

    # Results plus text
    result = recognizer.FinalResult()
    trascrizione += result
    logging.info("Trascrizione completata")
    
    return trascrizione

if __name__ == "__main__":
    # Path to your wav
    file_wav = r"/home/teo/Project/MP3ToText/audio_16khz.wav"  # Sostituisci con il tuo percorso del file WAV
    # Path to the vosk model
    model_path = r"/home/teo/Project/MP3ToText/vosk"  # Sostituisci con il percorso del modello Vosk

    try:
        # transcription
        trascrizione = trascrivi_audio_vosk(file_wav, model_path)
        
        # Output 
        print("Trascrizione:\n", trascrizione)
    
    except Exception as e:
        logging.error(f"Errore nel processo di trascrizione: {e}")