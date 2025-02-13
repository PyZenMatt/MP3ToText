# Mp3ToText

**Mp3ToText** is a Python tool that converts MP3 (and M4A) audio files into text using speech recognition via the Vosk model. This project is designed to be easy to use, customizable, and portable, making it ideal for automatic audio transcription. The tool now includes a **Graphical User Interface (GUI)** for a more user-friendly experience.

## Features

- **Support for MP3 and M4A files**: Automatic conversion of audio files to WAV format with 16 kHz sample rate.
- **Offline speech recognition**: Uses the Vosk model for transcription, no internet connection required.
- **Audio enhancement**: Volume normalization, noise reduction, and setting optimal audio frequency.
- **Graphical User Interface (GUI)**: Intuitive interface for easy file loading, conversion, and transcription.
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
    ```

4. **Download the Vosk model**:
    Download a Vosk model from the official website [here](https://alphacephei.com/vosk/models) and place it in the appropriate directory.

## Usage

### Using the GUI

1. **Run the GUI**:
    ```bash
    python main.py
    ```

2. **Load an MP3 or M4A file**:
    - Click on "Carica MP3/M4A" to load an audio file.
    - The file will be automatically converted to WAV format with a 16 kHz sample rate.

3. **Transcribe the WAV file**:
    - Click on "Carica WAV per Trascrizione" to load a WAV file.
    - The transcription will appear in the text area.

### Using the Command Line

1. **Convert an MP3 or M4A file to WAV**:
    Run the program with the path to your audio file:
    ```bash
    python mp3_to_wav.py
    ```

2. **Transcribe the WAV file**:
    Run the transcription script:
    ```bash
    python script_vosk.py
    ```

3. **The transcription will be shown on the screen**. You can also modify the code to save the transcription in a `.txt` file or another format.

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
- **Tkinter**: Used for the graphical user interface.

---

## **Sezione in italiano**

**Mp3ToText** è uno strumento Python che converte file audio in formato **MP3** (e **M4A**) in testo tramite il riconoscimento vocale, utilizzando il modello Vosk. Il progetto è pensato per essere facilmente utilizzabile, personalizzabile e portatile, ideale per attività di trascrizione automatica di audio. Ora include anche un'interfaccia grafica (GUI) per un'esperienza più user-friendly.

### **Caratteristiche**

- **Supporto per file MP3 e M4A**: Conversione automatica dei file audio in formato WAV con frequenza di campionamento di 16 kHz.
- **Riconoscimento vocale offline**: Utilizzo del modello Vosk per la trascrizione, senza necessità di connessione a Internet.
- **Miglioramento audio**: Normalizzazione del volume, riduzione del rumore e impostazione della frequenza audio ottimale.
- **Interfaccia Grafica (GUI)**: Interfaccia intuitiva per il caricamento dei file, la conversione e la trascrizione.
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

4. **Scarica il modello Vosk**:
    Scarica un modello Vosk dal sito ufficiale [qui](https://alphacephei.com/vosk/models) e posizionalo nella directory appropriata.

### **Come usare**

#### Utilizzo della GUI

1. **Esegui la GUI**:
    ```bash
    python main.py
    ```

2. **Carica un file MP3 o M4A**:
    - Clicca su "Carica MP3/M4A" per caricare un file audio.
    - Il file verrà automaticamente convertito in formato WAV con una frequenza di campionamento di 16 kHz.

3. **Trascrivi il file WAV**:
    - Clicca su "Carica WAV per Trascrizione" per caricare un file WAV.
    - La trascrizione apparirà nell'area di testo.

#### Utilizzo da riga di comando

1. **Converti un file MP3 o M4A in WAV**:
    Esegui il programma con il percorso del tuo file audio:
    ```bash
    python mp3_to_wav.py
    ```

2. **Trascrivi il file WAV**:
    Esegui lo script di trascrizione:
    ```bash
    python script_vosk.py
    ```

3. **La trascrizione sarà mostrata a schermo**. Puoi anche modificare il codice per salvare la trascrizione su un file `.txt` o altro formato.

### **Esempio d'uso**

Supponiamo di avere un file chiamato `audio.mp3`:

1. Esegui la conversione e la trascrizione con il comando:
    ```bash
    python script_vosk.py
    ```
2. Dopo l'esecuzione, il programma mostrerà la trascrizione dell'audio.

### **Contribuire**

Se desideri contribuire al progetto, segui questi passaggi:

1. **Fork** del repository.
2. **Crea un branch** per la tua funzionalità (`git checkout -b feature/nome-funzionalita`).
3. **Fai commit** delle tue modifiche (`git commit -m 'Aggiunta nuova funzionalità'`).
4. **Push** del tuo branch (`git push origin feature/nome-funzionalita`).
5. **Crea una pull request**.

### **Licenza**

Questo progetto è distribuito sotto la **MIT License**. Vedi il file [LICENSE](LICENSE) per ulteriori dettagli.

### **Contatti**

- Autore: [Matteo Ricci](https://github.com/PyZenMatt)
- Email: matteoricci12@outlook.it

### **Tecnologie utilizzate**

- **Python**: Linguaggio di programmazione principale.
- **Vosk**: Riconoscimento vocale offline.
- **pydub**: Manipolazione e conversione dei file audio.
- **ffmpeg**: Utilizzato per la conversione tra formati audio.
- **Tkinter**: Utilizzato per l'interfaccia grafica.
