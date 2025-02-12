# Mp3ToText

**Mp3ToText** is a Python tool that converts MP3 (and M4A) audio files into text using speech recognition via the Vosk model. This project is designed to be easy to use, customizable, and portable, making it ideal for automatic audio transcription.

## Features

- **Support for MP3 and M4A files**: Automatic conversion of audio files to WAV format with 16 kHz sample rate.
- **Offline speech recognition**: Uses the Vosk model for transcription, no internet connection required.
- **Audio enhancement**: Volume normalization, noise reduction, and setting optimal audio frequency.
- **Easy to use**: Simply provide the audio file path, and the program will return the transcription.

## Installation

To use Mp3ToText, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Mp3ToText.git
    ```

2. **Install the dependencies**:
    You can install all the necessary dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Make sure ffmpeg is installed** (required for audio conversion):
    - On **Windows**, download it from [here](https://ffmpeg.org/download.html) and add the `ffmpeg` path to your `PATH` environment variable.
    - On **macOS** or **Linux**, you can install it using your package manager:
    ```bash
    brew install ffmpeg

4 Make sure to get the (free) model vosk you like from the official website https://alphacephei.com/vosk/models
    ```

## Usage

1. **Convert an MP3 or M4A file to WAV**:
   Run the program with the path to your audio file:
    ```bash
    python mp3_to_wav.py
    ```

2. **The transcription will be shown on the screen**. You can also modify the code to save the transcription in a `.txt` file or another format.

## Example

Given an audio file called `audio.mp3`:

1. Run the conversion and transcription with the command:
    ```bash
    python script_vosk.py
    ```
2. After running, the program will display the transcription of the audio.

## Contributing

If you want to contribute to the project, please follow these steps:

1. **Fork** the repository.
2. **Create a branch** for your feature (`git checkout -b feature/your-feature`).
3. **Commit** your changes (`git commit -m 'Added new feature'`).
4. **Push** your branch (`git push origin feature/your-feature`).
5. **Create a pull request**.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Contact

- Author: [Matteo Ricci](https://github.com/PyZenMatt)
- Email: matteoricci12@outlook.it


## Technologies used

- **Python**: The main programming language.
- **Vosk**: Offline speech recognition model.
- **pydub**: Audio file manipulation and conversion.
- **ffmpeg**: Used for format conversion.

---

## **Sezione in italiano**

**Mp3ToText** è uno strumento Python che converte file audio in formato **MP3** (e **M4A**) in testo tramite il riconoscimento vocale, utilizzando il modello Vosk. Il progetto è pensato per essere facilmente utilizzabile, personalizzabile e portatile, ideale per attività di trascrizione automatica di audio.

### **Caratteristiche**

- **Supporto per file MP3 e M4A**: Conversione automatica dei file audio in formato WAV con frequenza di campionamento di 16 kHz.
- **Riconoscimento vocale offline**: Utilizzo del modello Vosk per la trascrizione, senza necessità di connessione a Internet.
- **Miglioramento audio**: Normalizzazione del volume, riduzione del rumore e impostazione della frequenza audio ottimale.
- **Facile da usare**: Basta inserire il percorso del file audio e il programma fornirà la trascrizione.

### **Installazione**

Per utilizzare Mp3ToText, segui questi passaggi:

1. **Clona il repository**:
    ```bash
    git clone https://github.com/tuo-utente/Mp3ToText.git
    ```

2. **Installa le dipendenze**:
    Puoi installare tutte le dipendenze necessarie utilizzando `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Assicurati di avere ffmpeg** (necessario per la conversione audio):
    - Su **Windows**, puoi scaricarlo da [qui](https://ffmpeg.org/download.html) e aggiungere il percorso di `ffmpeg` alla variabile d'ambiente `PATH`.
    - Su **macOS** o **Linux**, puoi installarlo tramite Homebrew o il package manager preferito:
    ```bash
    brew install ffmpeg
    ```

### **Come usare**

1. **Convertono un file audio MP3 o M4A in formato WAV**:
   Esegui il programma con il percorso del tuo file audio:
    ```bash
    python script_vosk.py
    ```

2. **La trascrizione sarà mostrata a schermo**. Puoi anche modificare il codice per salvare la trascrizione su un file `.txt` o altro formato.

### **Esempio d'uso**

Supponiamo di avere un file chiamato `audio.mp3`:

1. Esegui la conversione e la trascrizione con il comando:
    ```bash
    python script_vosk.py
    ```
2. Dopo l'esecuzione, il programma mostrerà la trascrizione dell'audio.


# Mp3ToText

**Mp3ToText** è uno strumento Python che converte file audio in formato **MP3** (e **M4A**) in testo tramite il riconoscimento vocale, utilizzando il modello Vosk. Il progetto è pensato per essere facilmente utilizzabile, personalizzabile e portatile, ideale per attività di trascrizione automatica di audio.

## Caratteristiche

- **Supporto per file MP3 e M4A**: Conversione automatica dei file audio in formato WAV con frequenza di campionamento di 16 kHz.
- **Riconoscimento vocale offline**: Utilizzo del modello Vosk per la trascrizione, senza necessità di connessione a Internet.
- **Miglioramento audio**: Normalizzazione del volume, riduzione del rumore e impostazione della frequenza audio ottimale.
- **Facile da usare**: Basta inserire il percorso del file audio e il programma fornirà la trascrizione.

## Installazione

Per utilizzare Mp3ToText, segui questi passaggi:

1. **Clona il repository**:
    ```bash
    git clone https://github.com/tuo-utente/Mp3ToText.git
    ```

2. **Installa le dipendenze**:
    Puoi installare tutte le dipendenze necessarie utilizzando `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    Il file `requirements.txt` include tutte le librerie necessarie, tra cui `pydub`, `vosk`, e `speechrecognition`.

3. **Assicurati di avere ffmpeg** (necessario per la conversione audio):
    - Su **Windows**, puoi scaricarlo da [qui](https://ffmpeg.org/download.html) e aggiungere il percorso di `ffmpeg` alla variabile d'ambiente `PATH`.
    - Su **macOS** o **Linux**, puoi installarlo tramite Homebrew o il package manager preferito:
    ```bash
    brew install ffmpeg
    ```

## Come usare

1. **Convertono un file audio MP3 o M4A in formato WAV**:
   Esegui il programma con il percorso del tuo file audio:
    ```bash
    python script_vosk.py
    ```

2. **La trascrizione sarà mostrata a schermo**. Puoi anche modificare il codice per salvare la trascrizione su un file `.txt` o altro formato.

## Esempio d'uso

Supponiamo di avere un file chiamato `audio.mp3`:

1. Esegui la conversione da mp3 a wav:
```bash
    mp3_to_wav.py
    ``

2 la trascrizione con il comando:
    ```bash
    python script_vosk.py
    ```
2. Dopo l'esecuzione, il programma mostrerà la trascrizione dell'audio.

## Contribuire

Se desideri contribuire al progetto, segui questi passaggi:

1. **Fork** del repository.
2. **Crea un branch** per la tua funzionalità (`git checkout -b feature/nome-funzionalita`).
3. **Fai commit** delle tue modifiche (`git commit -m 'Aggiunta nuova funzionalità'`).
4. **Push** del tuo branch (`git push origin feature/nome-funzionalita`).
5. **Crea una pull request**.

## Licenza

Questo progetto è distribuito sotto la **MIT License**. Vedi il file [LICENSE](LICENSE) per ulteriori dettagli.

## Contatti

- Autore: [Matteo Ricci](https://github.com/PyZenMatt)
- Email: info@matteoricci.net


## Tecnologie utilizzate

- **Python**: Linguaggio di programmazione principale.
- **Vosk**: Riconoscimento vocale offline.
- **pydub**: Manipolazione e conversione dei file audio.
- **ffmpeg**: Utilizzato per la conversione tra formati audio.
