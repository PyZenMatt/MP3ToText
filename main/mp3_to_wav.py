from pydub import AudioSegment
import os

def converti_mp3_in_wav(file_mp3):
    audio = AudioSegment.from_mp3(file_mp3)
    audio = audio.normalize()
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)

    file_wav = file_mp3.replace(".mp3", "_16khz.wav")
    
    if os.path.exists(file_wav):
        raise Exception(f"Il file {file_wav} esiste già!")
    
    audio.export(file_wav, format="wav")
    return file_wav

if __name__ == "__main__":
    file_mp3 = r"/home/teo/Project/MP3ToText/audio.mp3"  # Sostituisci con il percorso corretto
    file_wav = converti_mp3_in_wav(file_mp3)
    print(f"✅ File WAV created! {file_wav}")
