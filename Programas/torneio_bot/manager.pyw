import tkinter as tk
from db import Conection

class Tela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        
        # frames
        frame = tk.Frame(self)
        
        # smogon
        smogon_frame = tk.Frame(frame)
        
        def smogon_unlock():
            if smogon_lock['text'] == "🔓":
                smogon_lock["text"] = "🔒"
                smogon_lock.config(bg="red")
            else:
                smogon_lock["text"] = "🔓"
                smogon_lock.config(bg="white")
            
        smogon_lock = tk.Button(smogon_frame, text="🔓", relief=tk.FLAT, command=smogon_unlock)
        smogon_lock.pack()
        
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
        
        def jf_unlock():
            if jf_lock['text'] == "🔓":
                jf_lock["text"] = "🔒"
                jf_lock.config(bg="red")
            else:
                jf_lock["text"] = "🔓"
                jf_lock.config(bg="white")
            
        jf_lock = tk.Button(jf_frame, text="🔓", relief=tk.FLAT, command=jf_unlock)
        jf_lock.pack()
        
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
        
        def gi_unlock():
            if gi_lock['text'] == "🔓":
                gi_lock["text"] = "🔒"
                gi_lock.config(bg="red")
            else:
                gi_lock["text"] = "🔓"
                gi_lock.config(bg="white")
            
        gi_lock = tk.Button(gi_frame, text="🔓", relief=tk.FLAT, command=gi_unlock)
        gi_lock.pack()
        
        
        gi_label = tk.Label(gi_frame, text="Giovana")
        gi_label.pack(side=tk.TOP)
                
        gi_button = tk.Button(gi_frame, text="-", command=lambda: self.diminuir("2"))
        gi_button.pack(side=tk.LEFT)
        self.gi_points = tk.Label(gi_frame, text=0)
        self.gi_points.pack(side=tk.LEFT)        
        gi_button_ = tk.Button(gi_frame, text="+", command=lambda: self.aumentar("2"))
        gi_button_.pack(side=tk.LEFT)
        
        gi_frame.pack(side=tk.LEFT, padx=10)
        
        # kedao
        kedao_frame = tk.Frame(frame)
        
        def kedao_unlock():
            if kedao_lock['text'] == "🔓":
                kedao_lock["text"] = "🔒"
                kedao_lock.config(bg="red")
            else:
                kedao_lock["text"] = "🔓"
                kedao_lock.config(bg="white")
            
        kedao_lock = tk.Button(kedao_frame, text="🔓", relief=tk.FLAT, command=kedao_unlock)
        kedao_lock.pack()
        
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
        
        send_button = tk.Button(frame, text="Enviar dados", command=self.enviar_pontos)
        send_button.pack()
    
        
        self.mainloop()
        
    def enviar_pontos(self):
        pontos = {
            "smogon": int(self.smogon_points['text']),
            "jf": int(self.jf_points['text']),
            "giovana": int(self.gi_points['text']),
            "kedao": int(self.kedao_points['text'])
        }
        
        cn = Conection()
        
        cn.inserir(pontos)
        
        
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
        
Tela()