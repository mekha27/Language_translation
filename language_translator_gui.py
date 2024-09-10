import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Supported languages for translation
LANGUAGES = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-cn",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
}

# Function to translate text
def translate_text():
    source_text = text_entry.get("1.0", tk.END).strip()  # Get text from the Text widget
    dest_lang = LANGUAGES[dest_lang_combo.get()]  # Get selected language from combo box
    
    if source_text:
        try:
            translated = translator.translate(source_text, dest=dest_lang)
            result_label.config(text=f"Translated Text: {translated.text}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="Please enter some text to translate.")

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")  # Set the size of the window
root.configure(bg="#f0f0f0")  # Background color

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0", foreground="#333")
style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
style.configure("TCombobox", padding=5, font=("Arial", 12))
style.configure("TFrame", background="#f0f0f0")

# Create a frame for padding and layout
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Title label
title_label = ttk.Label(frame, text="Language Translator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Text input field
text_entry_label = ttk.Label(frame, text="Enter text to translate:")
text_entry_label.pack(pady=5)
text_entry = tk.Text(frame, height=5, width=50, font=("Arial", 12))
text_entry.pack(pady=5)

# Dropdown for selecting the target language
dest_lang_label = ttk.Label(frame, text="Select destination language:")
dest_lang_label.pack(pady=5)
dest_lang_combo = ttk.Combobox(frame, values=list(LANGUAGES.keys()), state="readonly", font=("Arial", 12))
dest_lang_combo.set("French")  # Default value
dest_lang_combo.pack(pady=5)

# Button to trigger translation
translate_button = ttk.Button(frame, text="Translate", command=translate_text)
translate_button.pack(pady=15)

# Label to display the result
result_label = ttk.Label(frame, text="", wraplength=400, font=("Arial", 12), background="#f0f0f0")
result_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()
