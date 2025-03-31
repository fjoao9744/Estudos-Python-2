import customtkinter as ctk

ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.state("zoomed")

button = ctk.CTkButton(app).pack(pady=(10, 0))

check = ctk.CTkCheckBox(app).pack(pady=(10, 0))

combo = ctk.CTkComboBox(app).pack(pady=(10, 0))

entry = ctk.CTkEntry(app).pack(pady=(10, 0))

option = ctk.CTkOptionMenu(app).pack(pady=(10, 0))

progress = ctk.CTkProgressBar(app).pack(pady=(10, 0))

radio = ctk.CTkRadioButton(app).pack(pady=(10, 0))

slider = ctk.CTkSlider(app).pack(pady=(10, 0))

switch = ctk.CTkSwitch(app).pack(pady=(10, 0))

tabview = ctk.CTkTabview(app).pack(pady=(10, 0))

textbox = ctk.CTkTextbox(app).pack(pady=(10, 0))

app.mainloop()

