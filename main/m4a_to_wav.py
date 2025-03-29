from pydub import AudioSegment
import os

def convert_m4a_in_wav(file_m4a):
    audio = AudioSegment.from_file(file_m4a, format="m4a")
    audio = audio.normalize()
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)

    file_wav = file_m4a.replace(".m4a", "_16khz.wav")
    
    if os.path.exists(file_wav):
        raise Exception(f"Il file {file_wav} esiste già!")
    
    audio.export(file_wav, format="wav")
    return file_wav

if __name__ == "__main__":
    file_m4a = r"path/to/your/file"  # Sostituisci con il percorso corretto
    file_wav = convert_m4a_in_wav(file_m4a)
    print(f"✅ File WAV created! {file_wav}")
