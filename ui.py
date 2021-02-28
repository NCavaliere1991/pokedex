from tkinter import *
import csv
from PIL import Image, ImageTk, ImageChops
from urllib.request import urlopen
from io import BytesIO


class PokedexInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Pokedex")
        self.window.config(padx=20, pady=20, bg="red")

        self.top_label = Label(text="Pokedex", fg='yellow', bg="red", font=('Pokemon Solid', 30, 'bold'))
        self.top_label.grid(column=0, row=0)

        self.name_label = Label(text="Choose your Pokemon:", fg='white', bg='red',
                                font=('Pokemon Solid', 20, 'bold'))
        self.name_label.grid(column=0, row=2)
        self.name_entry = Entry(highlightthickness=0)
        self.name_entry.grid(column=0, row=3)
        self.button = Button(text="Get Info", command=self.get_entry, highlightthickness=0, bg='red', fg='green')
        self.button.grid(column=0, row=4, pady=10)
        self.name = Label(text="", fg="white", bg="red", font=('Pokemon Solid', 20))
        self.name.grid(column=0, row=6)
        self.type_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.type_label.grid(column=0, row=7)
        self.basexp_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.basexp_label.grid(column=0, row=8)
        self.height_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.height_label.grid(column=0, row=9)
        self.weight_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.weight_label.grid(column=0, row=10)
        self.hp_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.hp_label.grid(column=0, row=11)
        self.attack_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.attack_label.grid(column=0, row=12)
        self.defense_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.defense_label.grid(column=0, row=13)
        self.sp_attack_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.sp_attack_label.grid(column=0, row=14)
        self.sp_defense_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.sp_defense_label.grid(column=0, row=15)
        self.speed_label = Label(text="", fg='white', bg='red', font=('Pokemon Solid', 20))
        self.speed_label.grid(column=0, row=16)

        self.window.mainloop()

    def get_entry(self):
        with open("pokedex_entries.csv") as poke_file:
            reader = csv.reader(poke_file)
            choice = self.name_entry.get()
            for row in reader:
                if choice.lower() == row[1]:
                    self.name.config(text=f'Name: {row[1].title()}')
                    self.type_label.config(text=f'Type: {row[2].title()}')
                    self.basexp_label.config(text=f'Base Exp: {row[3]}')
                    self.height_label.config(text=f'Height: {row[4]}dm')
                    self.weight_label.config(text=f'Weight: {row[5]}dg')
                    self.hp_label.config(text=f'HP: {row[6]}')
                    self.attack_label.config(text=f'Attack: {row[7]}')
                    self.defense_label.config(text=f'Defense: {row[8]}')
                    self.sp_attack_label.config(text=f'Special Attack: {row[9]}')
                    self.sp_defense_label.config(text=f'Special Defense: {row[10]}')
                    self.speed_label.config(text=f'Speed: {row[11]}')

                    url = f'{row[12]}'
                    u = urlopen(url)
                    poke_img = BytesIO(u.read())
                    pil_img = Image.open(poke_img)
                    tk_img = ImageTk.PhotoImage(pil_img)

                    self.poke_pic = Label(image=tk_img, bg='green3', height=96, width=96)
                    self.poke_pic.image = tk_img
                    self.poke_pic.grid(column=0, row=5)

