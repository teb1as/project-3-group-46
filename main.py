import tkinter as tk
from gui import CelebLookalikeGUI
import csv
import os

# HashMap: storing celebrity attributes
def load_attributes(file_path):
    attributes = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            celeb_id = row['image_id']
            attributes[celeb_id] = {key: (value == '1') for key, value in row.items() if key != 'image_id'}
    return attributes

# graph implementation using dictionaries
class CelebrityGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, celeb_id):
        if celeb_id not in self.graph:
            self.graph[celeb_id] = []

    def add_edge(self, celeb_id_1, celeb_id_2, weight):
        if celeb_id_1 in self.graph and celeb_id_2 in self.graph:
            self.graph[celeb_id_1].append((celeb_id_2, weight))
            self.graph[celeb_id_2].append((celeb_id_1, weight))

    def get_neighbors(self, celeb_id):
        return self.graph.get(celeb_id, [])

    def get_similarity(self, celeb_id_1, celeb_id_2):
        for neighbor, weight in self.graph.get(celeb_id_1, []):
            if neighbor == celeb_id_2:
                return weight
        return

# calculate similarity (Hamming distance)
def calculate_similarity(user_features, celeb_features):
    score = 0
    for feature, value in user_features.items():
        if celeb_features.get(feature) == value:
            score += 1
    return score

# find lookalikes based on similarity
def find_lookalikes(user_features, celebrity_attributes, celeb_graph):
    lookalikes = []
    for celeb_id, celeb_features in celebrity_attributes.items():
        similarity = calculate_similarity(user_features, celeb_features)
        lookalikes.append((celeb_id, similarity))
        celeb_graph.add_node(celeb_id)
        celeb_graph.add_edge('user', celeb_id, similarity)
    lookalikes.sort(key=lambda x: x[1], reverse=True)
    return lookalikes

def calculate_similarity_percentage(user_features, celeb_features):
    matching_features = 0
    total_features = len(user_features)
    for feature, value in user_features.items():
        if celeb_features.get(feature) == value:
            matching_features += 1
            
    # Calculate the percentage of matching features
    if total_features == 0:
        return 0.0  # Avoid division by zero if no features provided
    similarity_percentage = (matching_features / total_features) * 100
    print(similarity_percentage)
    return similarity_percentage

def main():
    # load celebrity data
    celeb_attributes = load_attributes('list_attr_celeba.csv')
    image_dir = 'img_align_celeba'

    # initialize the graph
    celeb_graph = CelebrityGraph()

    # create the main window and the GUI
    root = tk.Tk()
    gui = CelebLookalikeGUI(root)

    hair_color_percentages = {
        'Blond Hair': 29983/202599,
        'Black Hair': 48472/202599,
        'Brown Hair': 41572/202599,
        'Gray Hair': 8499/202599
    }

    gender_percentages = {
        'Male': 84434/202599,
        'Female': 118165/202599
    }

    facial_hair_percentages = {
        '5 o Clock Shadow': 22516/202599,
        'Goatee': 12716/202599,
        'Mustache': 8417/202599,
        'No Beard': 169158/202599
    }

    similarity_label = tk.Label(root, text="", font=("Arial", 14), bg="darkslategray", fg="white")
    similarity_label.place(x=50, y=500)
    match_percentage_label = tk.Label(root, text="", font=("Arial", 14), bg="darkslategray", fg="white")
    match_percentage_label.place(x=725 + (400 - match_percentage_label.winfo_reqwidth()) // 2, y=600)

    def update_image():
        # get user input
        user_input = gui.get_user_input()
        hair_color = None
        male_or_female = None
        facial_hair = None

        lookalikes = find_lookalikes(user_input, celeb_attributes, celeb_graph)
        if lookalikes:
            first_match = lookalikes[0][0]
            img_path = os.path.join(image_dir, first_match)
            if os.path.exists(img_path):
                gui.update_image(img_path)

        first_lookalike_attributes = celeb_attributes.get(first_match)
        match_percentage = calculate_similarity_percentage(user_input, first_lookalike_attributes)
        match_percentage_label.config(text=f"Best Match: {match_percentage:.2f}%")
        # Determine the selected hair color
        for color, selected in user_input.items():
            if selected and color.replace('_', ' ') in hair_color_percentages:
                hair_color = color.replace('_', ' ')
                break
        
        # Determine gender
        male_or_female = 'Male' if user_input['Male'] == 1 else 'Female'
        
        # Determine facial hair
        for style, selected in user_input.items():
            if selected and style.replace('_', ' ') in facial_hair_percentages:
                facial_hair = style.replace('_', ' ')
                break

        # Update the similarity percentage based on most prominent physical features
        similarity_percentage = hair_color_percentages.get(hair_color, 0.0)*gender_percentages.get(male_or_female, 0.0)\
        *facial_hair_percentages.get(facial_hair, 0.0) * 100
        similarity_label.config(text=f"You look like {similarity_percentage:.2f}% of celebrities")

    # button to trigger the update image action
    find_button = tk.Button(root, text="Find Lookalike", command=update_image, font=("Arial", 14), width=20, height=2)
    find_button.place(x=50, y=439)
    # start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()