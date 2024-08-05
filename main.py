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
        return None


# calculate similarity
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


# main function to run the application
def main():
    # load celebrity data
    celeb_attributes = load_attributes('list_attr_celeba.csv')
    image_dir = 'img_align_celeba'

    # initialize the graph
    celeb_graph = CelebrityGraph()

    # Create the main window and the GUI
    root = tk.Tk()
    gui = CelebLookalikeGUI(root)

    def update_image():
        # get user input and find lookalikes
        user_input = gui.get_user_input()
        lookalikes = find_lookalikes(user_input, celeb_attributes, celeb_graph)
        if lookalikes:
            first_match = lookalikes[0][0]
            img_path = os.path.join(image_dir, first_match)
            if os.path.exists(img_path):
                gui.update_image(img_path)

    # button to trigger the update image action
    tk.Button(root, text="Find Lookalike", command=update_image).grid(column=1, row=5, padx=10, pady=10)

    # start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
