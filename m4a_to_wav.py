from pydub import AudioSegment

# Function to convert the file 
def convert_m4a_in_wav(file_m4a):
    # This Upload The File
    audio = AudioSegment.from_file(file_m4a, format="m4a")

    # This normalize the audio
    audio = audio.normalize()

    # Set frequency a 16 kHz, mono e sample width a 16-bit PCM
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)  # 16-bit PCM

    # Name of the file
    file_wav = file_m4a.replace(".m4a", "_16khz.wav")

    # Exporting the file
    audio.export(file_wav, format="wav")

    return file_wav

if __name__ == "__main__":
    # Your Path
    file_m4a = r"path/to/your/file"  # Sostituisci con il percorso corretto

    # Conversion
    file_wav = convert_m4a_in_wav(file_m4a)
    
    # Show results
    print(f"✅ File WAV Created: {file_wav}")
