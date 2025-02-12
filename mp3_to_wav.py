from pydub import AudioSegment

# Funzione per convertire MP3 in WAV con miglioramenti audio
def converti_mp3_in_wav(file_mp3):
    # Carica il file MP3
    audio = AudioSegment.from_mp3(file_mp3)

    # Miglioramento: Normalizzazione del volume
    audio = audio.normalize()

    # Imposta frequenza a 16 kHz, mono e sample width a 16-bit PCM
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)  # 16-bit PCM

    # Crea il nome del file WAV
    file_wav = file_mp3.replace(".mp3", "_16khz.wav")

    # Esporta il file come WAV con i parametri corretti
    audio.export(file_wav, format="wav")

    return file_wav

if __name__ == "__main__":
    # Percorso del file MP3
    file_mp3 = r"C:\Users\matte\OneDrive\Desktop\Script\Mp3ToText\audio.mp3"  # Sostituisci con il percorso corretto

    # Conversione da MP3 a WAV con miglioramenti
    file_wav = converti_mp3_in_wav(file_mp3)
    
    # Mostra il percorso del file WAV risultante
    print(f"✅ File WAV creato e migliorato: {file_wav}")
