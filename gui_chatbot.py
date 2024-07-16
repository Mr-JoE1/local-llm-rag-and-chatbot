import customtkinter as ctk
from chatbot import query_rag, MAX_INPUT_SIZE

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thinker Chatbot")
        self.root.geometry("600x600")
        ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.chat_display = ctk.CTkTextbox(master=self.frame, wrap="word", state='disabled', width=550, height=400)
        self.chat_display.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        self.user_input = ctk.CTkEntry(master=self.frame, placeholder_text="Type your question here...")
        self.user_input.grid(row=1, column=0, pady=10, padx=10, sticky="ew")
        self.user_input.bind("<Return>", self.send_message_event)

        self.send_button = ctk.CTkButton(master=self.frame, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        user_message = self.user_input.get()
        if len(user_message) > MAX_INPUT_SIZE:
            self.display_message(f"Error: Input exceeds the maximum allowed length of {MAX_INPUT_SIZE} characters.")
            return

        if user_message.strip():
            self.display_message(f"\nUser: {user_message}")
            self.user_input.delete(0, ctk.END)
            self.root.after(10, self.get_response, user_message)

    def get_response(self, user_message):
        response = query_rag(user_message)
        response_text, sources = self.extract_response_sources(response)
        self.display_message(f"\nAnswer: {user_message}")
        #if sources:
        self.display_message(f"\nSources: {sources}")

    def extract_response_sources(self, response):
        parts = response.split('\033[93mSources:')
        response_text = parts[0].strip()
        sources = parts[1].strip().rstrip('\033[0m') if len(parts) > 1 else ''
        return response_text, sources

    def display_message(self, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(ctk.END, message + "\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(ctk.END)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ChatbotApp(root)
    root.mainloop()
