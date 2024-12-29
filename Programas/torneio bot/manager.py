import tkinter as tk
from tkinter import ttk

class Tela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        
        # frames
        frame = tk.Frame(self)
        
        # smogon
        smogon_frame = tk.Frame(frame)
        
        smogon_label = tk.Label(smogon_frame, text="Smogon")
        smogon_label.pack(side=tk.TOP)
                
        smogon_button = tk.Button(smogon_frame, text="-", command=lambda: self.diminuir("0"))
        smogon_button.pack(side=tk.LEFT)
        self.smogon_points = tk.Label(smogon_frame, text=0)
        self.smogon_points.pack(side=tk.LEFT)        
        smogon_button_ = tk.Button(smogon_frame, text="+", command=lambda: self.aumentar("0"))
        smogon_button_.pack(side=tk.LEFT)
        
        smogon_frame.pack(side=tk.LEFT, padx=10)
        
        # jf     
        jf_frame = tk.Frame(frame)
        
        jf_label = tk.Label(jf_frame, text="JF")
        jf_label.pack(side=tk.TOP)
                
        jf_button = tk.Button(jf_frame, text="-", command=lambda: self.diminuir("1"))
        jf_button.pack(side=tk.LEFT)
        self.jf_points = tk.Label(jf_frame, text=0)
        self.jf_points.pack(side=tk.LEFT)        
        jf_button_ = tk.Button(jf_frame, text="+", command=lambda: self.aumentar("1"))
        jf_button_.pack(side=tk.LEFT)
        
        jf_frame.pack(side=tk.LEFT, padx=10)
        
        # gi    
        gi_frame = tk.Frame(frame)
        
        gi_label = tk.Label(gi_frame, text="Giovana")
        gi_label.pack(side=tk.TOP)
                
        gi_button = tk.Button(gi_frame, text="-", command=lambda: self.diminuir("2"))
        gi_button.pack(side=tk.LEFT)
        self.gi_points = tk.Label(gi_frame, text=0)
        self.gi_points.pack(side=tk.LEFT)        
        gi_button_ = tk.Button(gi_frame, text="+", command=lambda: self.aumentar("2"))
        gi_button_.pack(side=tk.LEFT)
        
        gi_frame.pack(side=tk.LEFT, padx=10)
        
        # gi    
        kedao_frame = tk.Frame(frame)
        
        kedao_label = tk.Label(kedao_frame, text="Kedao")
        kedao_label.pack(side=tk.TOP)
                
        kedao_button = tk.Button(kedao_frame, text="-", command=lambda: self.diminuir("3"))
        kedao_button.pack(side=tk.LEFT)
        self.kedao_points = tk.Label(kedao_frame, text=0)
        self.kedao_points.pack(side=tk.LEFT)        
        kedao_button_ = tk.Button(kedao_frame, text="+", command=lambda: self.aumentar("3"))
        kedao_button_.pack(side=tk.LEFT)
        
        kedao_frame.pack(side=tk.LEFT, padx=10)
        
        frame.pack()
        
        self.mainloop()
        
    def diminuir(self, tipo):
        match tipo:
            case "0":
                self.smogon_points["text"] -= 1
            case "1":
                self.jf_points["text"] -= 1
            case "2":
                self.gi_points["text"] -= 1
            case "3":
                self.kedao_points["text"] -= 1
                
    def aumentar(self, tipo):
        match tipo:
            case "0":
                self.smogon_points["text"] += 1
            case "1":
                self.jf_points["text"] += 1
            case "2":
                self.gi_points["text"] += 1
            case "3":
                self.kedao_points["text"] += 1
        



play = Tela()