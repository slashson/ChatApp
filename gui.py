import customtkinter as ctk
from customtkinter import CTkImage

from chat import send_message_to_model
from PIL import Image

class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.arrow = CTkImage(light_image=Image.open("icons/send.png"),size=(8, 8))
        self.title("DeepSeek Chat")
        self.geometry("440x540")
        self.configure(fg_color="#262627")

        self.chat_history = ctk.CTkScrollableFrame(self,
                                                   width=480,
                                                   height=440,
                                                   fg_color="#262627",
                                                   scrollbar_button_color="#333333",
                                                   scrollbar_button_hover_color="#404040"
                                                   )
        self.chat_history.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Ask something",
                                  width=408,
                                  height=48,
                                  font=("SF Pro Display", 14),
                                  text_color="#F4F4F4",
                                  fg_color="#2E2E2E",
                                  corner_radius=16,
                                  border_color="#4A4A4C"
                                  )
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.send_message)

        self.button = ctk.CTkButton(self, text="",
                                    image=self.arrow,
                                    corner_radius=13,
                                    width=26,
                                    height=26,
                                    fg_color="#D4D4D4",
                                    bg_color="#2E2E2E",
                                    command=self.send_message
                                    )
        self.button.place(x=376, y=496)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        user_message = ctk.CTkLabel(
            self.chat_history,
            text=user_input,
            text_color="#F4F4F4",
            fg_color="#414345",
            font=("SF Pro Display", 15),
            corner_radius=20,
            padx=2,
            pady=10,
            anchor="e",
            justify="right",
            wraplength=200
        )
        user_message.pack(pady=5, padx=10, anchor="e")
        self.entry.delete(0, "end")

        try:
            response = send_message_to_model(user_input)
            print(response)
            bot_message = ctk.CTkLabel(
                self.chat_history,
                text=response,
                fg_color="#262627",
                text_color="#F4F4F4",
                font=("SF Pro Display", 15),
                corner_radius=20,
                padx=2,
                pady=9,
                anchor="w",
                justify="left",
                wraplength=200
            )
            bot_message.pack(pady=5, padx=10, anchor="w")
            # нельзя копировать текст который отправляет бот
            # решения CTkTextbox или CTkLabel + bind забиндить копирования текста всего на нажатие ЛКМ по лейблу
        except Exception as e:
            print("end", f"\n❌ Ошибка: {e}\n")


if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()