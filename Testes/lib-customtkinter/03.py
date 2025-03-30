import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x300")

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = ctk.CTkOptionMenu(app, values=["option 1", "option 2"],
                                         command=optionmenu_callback)
optionmenu.set("option 2")
optionmenu.pack(pady=30)
app.mainloop()