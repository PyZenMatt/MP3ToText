from pydub import AudioSegment

# Funzione per convertire M4A in WAV con miglioramenti audio
def converti_m4a_in_wav(file_m4a):
    # Carica il file M4A
    audio = AudioSegment.from_file(file_m4a, format="m4a")

    # Miglioramento: Normalizzazione del volume
    audio = audio.normalize()

    # Imposta frequenza a 16 kHz, mono e sample width a 16-bit PCM
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)  # 16-bit PCM

    # Crea il nome del file WAV
    file_wav = file_m4a.replace(".m4a", "_16khz.wav")

    # Esporta il file come WAV con i parametri corretti
    audio.export(file_wav, format="wav")

    return file_wav

if __name__ == "__main__":
    # Percorso del file M4A
    file_m4a = r"C:\Users\matte\OneDrive\Desktop\Script\Mp3ToText\audio.m4a"  # Sostituisci con il percorso corretto

    # Conversione da M4A a WAV con miglioramenti
    file_wav = converti_m4a_in_wav(file_m4a)
    
    # Mostra il percorso del file WAV risultante
    print(f"✅ File WAV creato e migliorato: {file_wav}")
