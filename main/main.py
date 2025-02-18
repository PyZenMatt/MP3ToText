import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from m4a_to_wav import convert_m4a_in_wav
from mp3_to_wav import converti_mp3_in_wav
from script_vosk import trascrivi_audio_vosk
import threading

class AudioTranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mp3/M4A to Text Transcriber")
        self.root.geometry("800x600")
        
        self.create_widgets()
        self.current_file = ""
        self.model_path = ""
        self.transcription_result = ""  # Aggiunto per memorizzare il risultato
        
    def create_widgets(self):
        # Frame principale
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sezione selezione modello
        model_frame = ttk.LabelFrame(main_frame, text="Modello Vosk", padding=10)
        model_frame.pack(fill=tk.X, pady=5)

        ttk.Button(
            model_frame,
            text="Seleziona Modello Vosk",
            command=self.load_model
        ).pack(side=tk.LEFT, padx=5)

        self.model_status = ttk.Label(model_frame, text="Nessun modello selezionato")
        self.model_status.pack(side=tk.LEFT, padx=10)
        
        # Sezione conversione
        conv_frame = ttk.LabelFrame(main_frame, text="Conversione Audio", padding=10)
        conv_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(
            conv_frame,
            text="Carica MP3/M4A",
            command=self.load_audio_file
        ).pack(side=tk.LEFT, padx=5)
        
        self.conv_status = ttk.Label(conv_frame, text="Nessun file selezionato")
        self.conv_status.pack(side=tk.LEFT, padx=10)
        
        # Sezione trascrizione
        trans_frame = ttk.LabelFrame(main_frame, text="Trascrizione Audio", padding=10)
        trans_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Button(
            trans_frame,
            text="Carica WAV per Trascrizione",
            command=self.load_wav_file
        ).pack(anchor=tk.NW, pady=5)
        
        self.trans_status = ttk.Label(trans_frame, text="Nessun file WAV selezionato")
        self.trans_status.pack(anchor=tk.NW)
        
        # Area testo
        self.text_output = tk.Text(trans_frame, wrap=tk.WORD, height=15)
        self.text_output.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Barra di avanzamento
        self.progress = ttk.Progressbar(main_frame, mode="indeterminate")
        
    def load_model(self):
        model_dir = filedialog.askdirectory(title="Seleziona cartella modello Vosk")
        if model_dir:
            self.model_path = model_dir
            self.model_status.config(text=f"Modello caricato: {model_dir}")
            
    def load_audio_file(self):
        filetypes = (
            ("File Audio", "*.mp3 *.m4a"),
            ("Tutti i file", "*.*")
        )
        
        self.current_file = filedialog.askopenfilename(filetypes=filetypes)
        if self.current_file:
            self.start_conversion()
            
    def start_conversion(self):
        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start()
        
        threading.Thread(target=self.convert_file).start()
        
    def convert_file(self):
        try:
            if self.current_file.endswith(".mp3"):
                output_file = converti_mp3_in_wav(self.current_file)
            elif self.current_file.endswith(".m4a"):
                output_file = convert_m4a_in_wav(self.current_file)
            else:
                messagebox.showerror("Errore", "Formato file non supportato")
                return
            
            self.conv_status.config(text=f"File convertito: {output_file}")
            messagebox.showinfo("Successo", "Conversione completata!")
            
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la conversione: {str(e)}")
        finally:
            self.progress.stop()
            self.progress.pack_forget()
            
    def load_wav_file(self):
        filetypes = (("File WAV", "*.wav"),)
        wav_file = filedialog.askopenfilename(filetypes=filetypes)
        if wav_file:
            self.start_transcription(wav_file)
            
    def start_transcription(self, wav_file):
        if not self.model_path:
            messagebox.showerror("Errore", "Seleziona prima un modello Vosk!")
            return

        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start()
        self.text_output.delete(1.0, tk.END)
        
        threading.Thread(target=self.run_transcription, args=(wav_file,)).start()
        
    def run_transcription(self, wav_file):
        try:
            self.trans_status.config(text=f"Trascrizione in corso: {wav_file}")
            result = trascrivi_audio_vosk(wav_file, self.model_path)
            
            # Invio il risultato al main thread per il salvataggio
            self.root.after(0, lambda: self.save_transcription(result))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Errore", 
                f"Errore durante la trascrizione: {str(e)}"
            ))
        finally:
            self.root.after(0, self.cleanup_transcription)
    
    def save_transcription(self, result):
        """Gestisce il salvataggio della trascrizione in un file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")],
            title="Salva trascrizione come"
        )
        
        if not file_path:  # Utente ha annullato
            return
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(result)
            messagebox.showinfo("Successo", f"Trascrizione salvata in:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il salvataggio:\n{str(e)}")

    def cleanup_transcription(self):
        """Pulizia dopo la trascrizione"""
        self.progress.stop()
        self.progress.pack_forget()
        self.trans_status.config(text="Pronto per nuova trascrizione")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioTranscriberApp(root)
    root.mainloop()