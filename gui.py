import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_combobox(parent, label, options, row):
    # create label and combobox for each attribute
    tk.Label(parent, text=label, bg="dimgray", font=("Arial", 14)).grid(column=0, row=row, padx=10, pady=10,
                                                                        sticky=tk.W)
    combobox = ttk.Combobox(parent, values=options, state="readonly", font=("Arial", 12), width=20)
    combobox.grid(column=1, row=row, padx=10, pady=10, sticky=tk.W)
    combobox.current(0)  # set default selection
    return combobox


class CelebLookalikeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Celeb Lookalike")
        self.root.geometry("1200x800")
        self.root.configure(background="darkslategray")

        # project signature box
        self.canvas = tk.Canvas(self.root, width=250, height=100)
        self.canvas.place(x=50, y=600)
        self.canvas.create_rectangle(0, 0, 500, 500, fill="dimgray")
        self.canvas.create_text(10, 50, text="Project by Dylan Everett,\nTavian Douge,\nAnd Mark Cortez",
                                font=("Arial", 14), fill="white", anchor=tk.W)

        # title label
        self.title_label = tk.Label(self.root, text="CELEB LOOK-ALIKE", font=("Arial", 30), bg="darkslategray",
                                    fg="white")
        self.title_label.pack(pady=20)

        # create a frame for the comboboxes and color it
        self.left_frame = tk.Frame(self.root, bg="dimgray", width=350, height=400)
        self.left_frame.place(x=50, y=150)

        # combobox options for different attributes
        self.gender_options = ['Male', 'Female']
        self.hairstyle_options = ['Bald', 'Bangs', 'Receding Hairline', 'Straight Hair', 'Wavy Hair']
        self.facial_hair_options = ['5_o_Clock_Shadow', 'Goatee', 'Mustache', 'No Beard']
        self.hair_color_options = ['Black Hair', 'Blond Hair', 'Brown Hair', 'Gray Hair']
        self.accessories_options = ['Eyeglasses', 'Wearing Hat', 'Wearing Earrings']

        # create comboboxes for attribute selection
        self.gender_combobox = create_combobox(self.left_frame, "Gender", self.gender_options, 0)
        self.hairstyle_combobox = create_combobox(self.left_frame, "Hairstyle", self.hairstyle_options, 1)
        self.facial_hair_combobox = create_combobox(self.left_frame, "Facial Hair", self.facial_hair_options, 2)
        self.hair_color_combobox = create_combobox(self.left_frame, "Hair Color", self.hair_color_options, 3)
        self.accessories_combobox = create_combobox(self.left_frame, "Accessories", self.accessories_options, 4)

        # placeholder for the displayed image
        self.canvas2 = tk.Canvas(self.root, width=500, height=500)
        self.canvas2.place(x=675, y=150)
        self.canvas2.create_rectangle(0, 0, 500, 500, fill="dimgray")

        self.image_label = tk.Label(self.root)
        self.image_label.place(x=725, y=200, width=400, height=400)

        # set placeholder image
        self.set_placeholder_image()

    def set_placeholder_image(self):
        # load and display the placeholder image
        placeholder_image_path = "funnyface.PNG"
        self.update_image(placeholder_image_path)

    def update_image(self, img_path):
        # update the image displayed in the label
        image = Image.open(img_path).resize((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def get_user_input(self):
        # collect user input from comboboxes
        return {
            'Male': 1 if self.gender_combobox.get() == 'Male' else -1,
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
