import random
import tkinter as tk
from tkinter import messagebox

class NombreMagiqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Nombre Magique")

        self.nombre_magique = random.randint(1, 10)
        self.vies = 3

        self.label_instructions = tk.Label(root, text="J'ai choisi un nombre entre 1 et 10. Essayez de le deviner.")
        self.label_instructions.pack(pady=10)

        self.label_vies = tk.Label(root, text=f"Vies restantes: {self.vies}")
        self.label_vies.pack(pady=10)

        self.label_message = tk.Label(root, text="")
        self.label_message.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.buttons = []
        for i in range(1, 11):
            button = tk.Button(self.button_frame, text=str(i), command=lambda i=i: self.deviner(i))
            button.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)
            self.buttons.append(button)

        self.button_rejouer = tk.Button(root, text="Rejouer", command=self.rejouer, state=tk.DISABLED)
        self.button_rejouer.pack(pady=10)

    def deviner(self, devine):
        if devine < self.nombre_magique:
            self.label_message.config(text="Trop bas ! Essayez encore.")
        elif devine > self.nombre_magique:
            self.label_message.config(text="Trop haut ! Essayez encore.")
        else:
            self.label_message.config(text=f"Félicitations ! Vous avez deviné le nombre magique : {self.nombre_magique}")
            for button in self.buttons:
                button.config(state=tk.DISABLED)
            self.button_rejouer.config(state=tk.NORMAL)
            return

        self.vies -= 1
        self.label_vies.config(text=f"Vies restantes: {self.vies}")

        if self.vies == 0:
            self.label_message.config(text=f"Désolé, vous avez épuisé toutes vies. Le nombre magique était {self.nombre_magique}.")
            for button in self.buttons:
                button.config(state=tk.DISABLED)
            self.button_rejouer.config(state=tk.NORMAL)

    def rejouer(self):
        self.nombre_magique = random.randint(1, 10)
        self.vies = 3
        self.label_vies.config(text=f"Vies restantes: {self.vies}")
        self.label_message.config(text="")
        for button in self.buttons:
            button.config(state=tk.NORMAL)
        self.button_rejouer.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NombreMagiqueApp(root)
    root.mainloop()
