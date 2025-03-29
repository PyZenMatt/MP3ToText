import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from m4a_to_wav import convert_m4a_in_wav
from mp3_to_wav import converti_mp3_in_wav
from script_vosk import trascrivi_audio_vosk
import threading
import queue
import os

class AudioTranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mp3/M4A to Text Transcriber")
        self.root.geometry("800x600")
        
        # Inizializzazione sistema thread-safe
        self.conversion_queue = queue.Queue()
        self.transcription_queue = queue.Queue()
        self.running_conversion_threads = 0
        self.running_transcription_threads = 0
        self.max_threads = 4  # Thread concorrenti massimi
        self.lock = threading.Lock()
        
        self.create_widgets()
        self.current_files = []
        self.wav_files = []
        self.model_path = ""
        
        # Gestione chiusura finestra
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sezione modello Vosk
        model_frame = ttk.LabelFrame(main_frame, text="Modello Vosk", padding=10)
        model_frame.pack(fill=tk.X, pady=5)

        ttk.Button(
            model_frame,
            text="Seleziona Modello Vosk",
            command=self.load_model
        ).pack(side=tk.LEFT, padx=5)

        self.model_status = ttk.Label(model_frame, text="Nessun modello selezionato")
        self.model_status.pack(side=tk.LEFT, padx=10)
        
        # Sezione conversione audio
        conv_frame = ttk.LabelFrame(main_frame, text="Conversione Audio", padding=10)
        conv_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(
            conv_frame,
            text="Carica MP3/M4A",
            command=self.load_audio_file
        ).pack(side=tk.LEFT, padx=5)
        
        # Area stato conversione
        conv_status_frame = ttk.Frame(conv_frame)
        conv_status_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        self.conv_status = tk.Text(conv_status_frame, height=4, wrap=tk.WORD, 
                                 state='disabled', bg=self.root.cget('bg'), 
                                 relief=tk.FLAT)
        self.conv_status.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        scrollbar = ttk.Scrollbar(conv_status_frame, command=self.conv_status.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.conv_status['yscrollcommand'] = scrollbar.set
        self.update_conversion_display("Nessun file selezionato")
        
        # Sezione trascrizione
        trans_frame = ttk.LabelFrame(main_frame, text="Trascrizione Audio", padding=10)
        trans_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Button(
            trans_frame,
            text="Carica WAV per Trascrizione",
            command=self.load_wav_file
        ).pack(anchor=tk.NW, pady=5)
        
        # Area stato trascrizione
        trans_status_frame = ttk.Frame(trans_frame)
        trans_status_frame.pack(anchor=tk.NW, fill=tk.X)
        
        self.trans_status = tk.Text(trans_status_frame, height=4, wrap=tk.WORD,
                                  state='disabled', bg=self.root.cget('bg'),
                                  relief=tk.FLAT)
        self.trans_status.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        trans_scrollbar = ttk.Scrollbar(trans_status_frame, command=self.trans_status.yview)
        trans_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.trans_status['yscrollcommand'] = trans_scrollbar.set
        self.update_transcription_display("Nessun file WAV selezionato")
        
        # Area risultati trascrizione
        self.text_output = tk.Text(trans_frame, wrap=tk.WORD, height=10)
        self.text_output.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Barra di progresso
        self.progress = ttk.Progressbar(main_frame, mode="indeterminate")

    def load_model(self):
        model_dir = filedialog.askdirectory(title="Seleziona cartella modello Vosk")
        if model_dir:
            self.model_path = model_dir
            self.model_status.config(text=f"Modello caricato: {model_dir}")

    def load_audio_file(self):
        filetypes = (("File Audio", "*.mp3 *.m4a"), ("Tutti i file", "*.*"))
        new_files = filedialog.askopenfilenames(filetypes=filetypes)
        
        if new_files:
            self.current_files.extend(new_files)
            status_text = "Nuovi file in coda..." if self.current_files else "File in conversione..."
            self.update_conversion_display(status_text)
            self.start_conversion(new_files)

    def start_conversion(self, files_to_convert):
        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start()
        
        # Aggiungi i file alla coda
        for file in files_to_convert:
            self.conversion_queue.put(file)
        
        # Avvia i thread worker
        for _ in range(min(self.max_threads, len(files_to_convert))):
            threading.Thread(target=self.conversion_worker, daemon=True).start()

    def conversion_worker(self):
        while True:
            try:
                file_path = self.conversion_queue.get_nowait()
                with self.lock:
                    self.running_conversion_threads += 1
                self.convert_file(file_path)
            except queue.Empty:
                break
            finally:
                with self.lock:
                    self.running_conversion_threads -= 1
                    if self.running_conversion_threads == 0 and self.conversion_queue.empty():
                        self.root.after(0, self.finish_conversion)
                self.conversion_queue.task_done()

    def convert_file(self, file_path):
        try:
            if file_path.endswith(".mp3"):
                output_file = converti_mp3_in_wav(file_path)
            elif file_path.endswith(".m4a"):
                output_file = convert_m4a_in_wav(file_path)
            else:
                self.root.after(0, lambda: messagebox.showerror("Errore", "Formato non supportato"))
                return
            
            self.root.after(0, lambda: self.update_conversion_status(output_file))
            
        except Exception as e:
            error_msg = f"Errore durante la conversione di {os.path.basename(file_path)}:\n{str(e)}"
            self.root.after(0, lambda msg=error_msg: messagebox.showerror("Errore", msg))
        finally:
            self.root.after(0, self.check_queues)

    def update_conversion_display(self, message):
        self.conv_status.config(state='normal')
        self.conv_status.delete(1.0, tk.END)
        self.conv_status.insert(tk.END, message)
        self.conv_status.config(state='disabled')
        self.conv_status.see(tk.END)

    def update_conversion_status(self, output_file):
        self.conv_status.config(state='normal')
        current_text = self.conv_status.get(1.0, tk.END).strip()
        new_text = f"{current_text}\n• {output_file}" if current_text else f"• {output_file}"
        self.conv_status.delete(1.0, tk.END)
        self.conv_status.insert(tk.END, new_text)
        self.conv_status.config(state='disabled')
        self.conv_status.see(tk.END)

    def finish_conversion(self):
        self.progress.stop()
        self.progress.pack_forget()
        messagebox.showinfo("Completato", "Tutte le conversioni sono terminate!")

    def load_wav_file(self):
        filetypes = (("File WAV", "*.wav"),)
        new_files = filedialog.askopenfilenames(filetypes=filetypes)
        
        if new_files:
            self.wav_files.extend(new_files)
            self.update_transcription_display("File in coda per trascrizione...")
            self.start_transcription(new_files)

    def start_transcription(self, wav_files):
        if not self.model_path:
            messagebox.showerror("Errore", "Seleziona prima un modello Vosk!")
            return

        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start()
        self.text_output.delete(1.0, tk.END)
        
        # Aggiungi i file alla coda
        for file in wav_files:
            self.transcription_queue.put(file)
        
        # Avvia i thread worker
        for _ in range(min(self.max_threads, len(wav_files))):
            threading.Thread(target=self.transcription_worker, daemon=True).start()

    def transcription_worker(self):
        while True:
            try:
                wav_file = self.transcription_queue.get_nowait()
                with self.lock:
                    self.running_transcription_threads += 1
                self.run_transcription(wav_file)
            except queue.Empty:
                break
            finally:
                with self.lock:
                    self.running_transcription_threads -= 1
                    if self.running_transcription_threads == 0 and self.transcription_queue.empty():
                        self.root.after(0, self.cleanup_transcription)
                self.transcription_queue.task_done()

    def run_transcription(self, wav_file):
        try:
            self.root.after(0, lambda: self.update_transcription_status(wav_file, "in corso"))
            result = trascrivi_audio_vosk(wav_file, self.model_path)
            
            self.root.after(0, lambda: (
                self.text_output.insert(tk.END, f"\n\n=== Trascrizione di {os.path.basename(wav_file)} ===\n{result}"),
                self.update_transcription_status(wav_file, "completato"),
                self.save_transcription(result, wav_file)
            ))
            
        except Exception as e:
            error_msg = f"Errore durante la trascrizione:\n{str(e)}"
            self.root.after(0, lambda msg=error_msg: messagebox.showerror("Errore", msg))
            self.update_transcription_status(wav_file, "fallito")
        finally:
            self.root.after(0, self.check_queues)

    def update_transcription_display(self, message):
        self.trans_status.config(state='normal')
        self.trans_status.delete(1.0, tk.END)
        self.trans_status.insert(tk.END, message)
        self.trans_status.config(state='disabled')
        self.trans_status.see(tk.END)

    def update_transcription_status(self, wav_file, status):
        self.trans_status.config(state='normal')
        current_text = self.trans_status.get(1.0, tk.END)
        
        # Aggiorna lo stato mantenendo la cronologia
        lines = current_text.split('\n')
        new_lines = [f"• {os.path.basename(wav_file)} ({status})" 
                    if os.path.basename(wav_file) in line 
                    else line 
                    for line in lines if line.strip()]
        
        if not any(os.path.basename(wav_file) in line for line in lines):
            new_lines.append(f"• {os.path.basename(wav_file)} ({status})")
            
        self.trans_status.delete(1.0, tk.END)
        self.trans_status.insert(tk.END, '\n'.join(new_lines))
        self.trans_status.config(state='disabled')
        self.trans_status.see(tk.END)

    def save_transcription(self, result, wav_file):
        base_name = os.path.splitext(os.path.basename(wav_file))[0]
        default_filename = f"{base_name}_trascrizione.txt"
        save_dir = filedialog.askdirectory(title="Seleziona cartella per salvare")
        
        if not save_dir:
            return
        
        full_path = os.path.join(save_dir, default_filename)
        
        # Controllo sovrascrittura
        if os.path.exists(full_path):
            if not messagebox.askyesno("Conferma", f"Il file {default_filename} esiste già. Sovrascrivere?"):
                return
        
        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(result)
            messagebox.showinfo("Successo", f"Trascrizione salvata in:\n{full_path}")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il salvataggio:\n{str(e)}")

    def cleanup_transcription(self):
        self.progress.stop()
        self.progress.pack_forget()
        messagebox.showinfo("Completato", "Tutte le trascrizioni sono terminate!")

    def check_queues(self):
        """Controlla lo stato delle code periodicamente"""
        if self.conversion_queue.empty() and self.transcription_queue.empty():
            if self.running_conversion_threads == 0 and self.running_transcription_threads == 0:
                self.progress.stop()
                self.progress.pack_forget()

    def on_close(self):
        """Gestione chiusura finestra"""
        if self.running_conversion_threads > 0 or self.running_transcription_threads > 0:
            if messagebox.askokcancel("Uscita", "Operazioni in corso. Vuoi davvero uscire?"):
                self.root.destroy()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioTranscriberApp(root)
    root.mainloop()