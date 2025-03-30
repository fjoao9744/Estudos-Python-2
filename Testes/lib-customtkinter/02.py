import customtkinter as ctk

ctk.set_appearance_mode("System") # padrão
# System, Dark, Light
ctk.set_default_color_theme("blue") # padrão
# blue, dark-blue e green(você tambem pode criar seu proprio tema)

def swith_theme(): # Troca o tema 
    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("Light")
    
app = ctk.CTk()
app.geometry("300x300")

# as cores podem ser pelo nome(red, darkred) ou pelo codigo hexa
button = ctk.CTkButton(app, text="Theme Color", fg_color=("red", "blue"), command=swith_theme)
button.pack(pady=50)

app.mainloop()

