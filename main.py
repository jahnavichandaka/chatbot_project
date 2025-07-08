import tkinter as tk
from tkinter import scrolledtext
from chatbot_logic import get_bot_response
from utils import listen_voice
current_theme = "light"
def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return

    chat_window.insert(tk.END, f"You: {user_msg}\n", "user")
    bot_response = get_bot_response(user_msg)
    chat_window.insert(tk.END, f"ChatPy: {bot_response}\n\n", "bot")
    user_input.delete(0, tk.END)

def send_voice():
    chat_window.insert(tk.END, "🎙️ Listening...\n", "bot")
    voice_input = listen_voice()
    chat_window.insert(tk.END, f"You (voice): {voice_input}\n", "user")
    response = get_bot_response(voice_input)
    chat_window.insert(tk.END, f"ChatPy: {response}\n\n", "bot")

# GUI Setup
root = tk.Tk()
root.title("ChatPy - Your Assistant")
root.geometry("500x500")
root.config(bg="#f0f4f7")

# Chat Display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 11))
chat_window.place(x=20, y=20, width=460, height=350)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")
chat_window.insert(tk.END, "ChatPy: Hello! I'm ChatPy. Type or say 'bye' to exit.\n\n", "bot")

# Text Entry
user_input = tk.Entry(root, font=("Segoe UI", 11))
user_input.place(x=20, y=390, width=360, height=30)

# Buttons
send_btn = tk.Button(root, text="Send", font=("Segoe UI", 10, "bold"), bg="#4681f4", fg="white", command=send_message)
send_btn.place(x=400, y=390, width=80, height=30)

voice_btn = tk.Button(root, text="🎤 Voice", font=("Segoe UI", 10, "bold"), bg="#34a853", fg="white", command=send_voice)
voice_btn.place(x=20, y=430, width=460, height=30)
def toggle_theme():
    global current_theme

    if current_theme == "light":
        root.config(bg="#2e2e2e")
        chat_window.config(bg="#1e1e1e", fg="#ffffff", insertbackground="white")
        user_input.config(bg="#333333", fg="#ffffff", insertbackground="white")
        send_btn.config(bg="#4caf50", fg="white")
        voice_btn.config(bg="#4caf50", fg="white")
        theme_btn.config(text="🌞 Light Mode", bg="#555")
        current_theme = "dark"
    else:
        root.config(bg="#f0f4f7")
        chat_window.config(bg="white", fg="black", insertbackground="black")
        user_input.config(bg="white", fg="black", insertbackground="black")
        send_btn.config(bg="#4681f4", fg="white")
        voice_btn.config(bg="#34a853", fg="white")
        theme_btn.config(text="🌙 Dark Mode", bg="#ddd")
        current_theme = "light"
theme_btn = tk.Button(root, text="🌙 Dark Mode", font=("Segoe UI", 10, "bold"), command=toggle_theme)
theme_btn.place(x=20, y=465, width=460, height=30)
root.mainloop()
