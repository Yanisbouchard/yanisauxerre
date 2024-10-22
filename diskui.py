import tkinter as tk
from tkinter import messagebox

class Disk:
    def __init__(self, total, used):
        self.total = total  
        self.used = used    

    @property
    def used_perc(self):
        return self.used / self.total * 100  

def calculate_percentage():
    try:
       
        total = float(entry_total.get())
        used = float(entry_used.get())
        
     
        if used > total:
            raise ValueError("L'espace utilisé ne peut pas être supérieur à l'espace total.")
        
       
        disk = Disk(total, used)
        percentage = disk.used_perc
        
       
        messagebox.showinfo("Résultat", f"Pourcentage d'utilisation : {percentage:.2f}%")
    
    except ValueError as e:
        
        messagebox.showerror("Erreur", f"Erreur : {e}")


root = tk.Tk()
root.title("Calcul de pourcentage d'utilisation d'un disque")


label_total = tk.Label(root, text="Espace total (en Go) :")
label_total.pack(pady=5)

entry_total = tk.Entry(root)
entry_total.pack(pady=5)

label_used = tk.Label(root, text="Espace utilisé (en Go) :")
label_used.pack(pady=5)

entry_used = tk.Entry(root)
entry_used.pack(pady=5)


button_calculate = tk.Button(root, text="Calculer", command=calculate_percentage)
button_calculate.pack(pady=20)


root.mainloop()
