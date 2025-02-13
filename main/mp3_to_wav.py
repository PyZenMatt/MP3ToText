from pydub import AudioSegment

# Function for convert mp3 to wav
def converti_mp3_in_wav(file_mp3):
    # Uploading Mp3 file
    audio = AudioSegment.from_mp3(file_mp3)

    # Normalize the audio
    audio = audio.normalize()

    # Set frequency at 16 kHz, mono e sample width a 16-bit PCM
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)  # 16-bit PCM

    # Name of the file wav
    file_wav = file_mp3.replace(".mp3", "_16khz.wav")

    # Exporting file 
    audio.export(file_wav, format="wav")

    return file_wav

if __name__ == "__main__":
    # Mp3 Path
    file_mp3 = r"/home/teo/Project/MP3ToText/audio.mp3"  # Sostituisci con il percorso corretto

    # Converting file
    file_wav = converti_mp3_in_wav(file_mp3)
    
    # Show results
    print(f"✅ File WAV created! {file_wav}")
