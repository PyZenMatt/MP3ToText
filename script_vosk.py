import wave
import logging
from vosk import Model, KaldiRecognizer

# Configurazione del logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Funzione per trascrivere l'audio usando Vosk
def trascrivi_audio_vosk(file_wav, model_path):
    logging.info(f"Inizio trascrizione con Vosk per il file: {file_wav}")
    
    # Carica il modello Vosk
    model = Model(model_path)
    
    # Apri il file audio (deve essere WAV)
    wf = wave.open(file_wav, "rb")
    
    # Verifica la frequenza di campionamento del file audio
    if wf.getframerate() != 16000:
        logging.warning("La frequenza di campionamento non è 16 kHz, il modello potrebbe non funzionare correttamente.")
    
    # Crea il riconoscitore Kaldi
    recognizer = KaldiRecognizer(model, wf.getframerate())

    # Inizializza la trascrizione
    trascrizione = ""
    
    # Leggi i dati dell'audio a blocchi di 4000 frame
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break  # Fine del file audio
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            trascrizione += result  # Aggiungi il risultato alla trascrizione

    # Elenco finale dei risultati (incluso il testo)
    result = recognizer.FinalResult()
    trascrizione += result
    logging.info("Trascrizione completata")
    
    return trascrizione

if __name__ == "__main__":
    # Percorso del file audio WAV
    file_wav = r"C:\Users\matte\OneDrive\Desktop\Script\Mp3ToText\audio_16khz.wav"  # Sostituisci con il tuo percorso del file WAV
    # Percorso del modello Vosk (assicurati di aver scaricato il modello e di conoscere il percorso)
    model_path = r"C:\Users\matte\OneDrive\Desktop\Script\Mp3ToText\vosk"  # Sostituisci con il percorso del modello Vosk

    try:
        # Trascrizione audio con Vosk
        trascrizione = trascrivi_audio_vosk(file_wav, model_path)
        
        # Output della trascrizione
        print("Trascrizione:\n", trascrizione)
    
    except Exception as e:
        logging.error(f"Errore nel processo di trascrizione: {e}")