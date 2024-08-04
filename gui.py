import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class CelebLookalikeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Celeb Lookalike")
        self.root.geometry("1200x800")

        # combobox options for different attributes
        self.hairstyle_options = ['Bald', 'Bangs', 'Receding Hairline', 'Straight Hair', 'Wavy Hair']
        self.facial_hair_options = ['5_o_Clock_Shadow', 'Goatee', 'Mustache', 'No Beard']
        self.hair_color_options = ['Black Hair', 'Blond Hair', 'Brown Hair', 'Gray Hair']
        self.accessories_options = ['Eyeglasses', 'Wearing Hat', 'Wearing Earrings']

        # create comboboxes for attribute selection
        self.hairstyle_combobox = self.create_combobox("Hairstyle", self.hairstyle_options, 0)
        self.facial_hair_combobox = self.create_combobox("Facial Hair", self.facial_hair_options, 1)
        self.hair_color_combobox = self.create_combobox("Hair Color", self.hair_color_options, 2)
        self.accessories_combobox = self.create_combobox("Accessories", self.accessories_options, 3)

        # placeholder for the displayed image
        self.image_label = tk.Label(self.root)
        self.image_label.place(x=600, y=100, width=400, height=400)

    def create_combobox(self, label, options, row):
        # create label and combobox for each attribute
        tk.Label(self.root, text=label).grid(column=0, row=row, padx=10, pady=10, sticky=tk.W)
        combobox = ttk.Combobox(self.root, values=options, state="readonly")
        combobox.grid(column=1, row=row, padx=10, pady=10, sticky=tk.W)
        combobox.current(0)  # set default selection
        return combobox

    def update_image(self, img_path):
        # update the image displayed in the label
        image = Image.open(img_path).resize((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def get_user_input(self):
        # collect user input from comboboxes
        return {
            'Bald': self.hairstyle_combobox.get() == 'Bald',
            'Bangs': self.hairstyle_combobox.get() == 'Bangs',
            'Receding_Hairline': self.hairstyle_combobox.get() == 'Receding Hairline',
            'Straight_Hair': self.hairstyle_combobox.get() == 'Straight Hair',
            'Wavy_Hair': self.hairstyle_combobox.get() == 'Wavy Hair',
            '5_o_Clock_Shadow': self.facial_hair_combobox.get() == '5_o_Clock_Shadow',
            'Goatee': self.facial_hair_combobox.get() == 'Goatee',
            'Mustache': self.facial_hair_combobox.get() == 'Mustache',
            'No_Beard': self.facial_hair_combobox.get() == 'No Beard',
            'Black_Hair': self.hair_color_combobox.get() == 'Black Hair',
            'Blond_Hair': self.hair_color_combobox.get() == 'Blond Hair',
            'Brown_Hair': self.hair_color_combobox.get() == 'Brown Hair',
            'Gray_Hair': self.hair_color_combobox.get() == 'Gray Hair',
            'Eyeglasses': self.accessories_combobox.get() == 'Eyeglasses',
            'Wearing_Hat': self.accessories_combobox.get() == 'Wearing Hat',
            'Wearing_Earrings': self.accessories_combobox.get() == 'Wearing Earrings'
        }
