import csv
import pygame
from PIL import Image
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


# graph implementation
class CelebrityGraph:
    def __init__(self):
        self.graph = {}  # initialize empty dictionary to store the graph

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
        return None  # no direct connection found


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
        celeb_graph.add_edge('user', celeb_id, similarity)  # connect user to celebrities based on similarity
    lookalikes.sort(key=lambda x: x[1], reverse=True)
    return lookalikes


# load an image using PIL and convert it to a format usable by pygame
def load_image(image_path):
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((200, 200))  # Resize if needed
    mode = pil_image.mode
    size = pil_image.size
    data = pil_image.tobytes()

    return pygame.image.fromstring(data, size, mode)


# GUI to get user input and display results
def main():
    celeb_attributes = load_attributes('list_attr_celeba.csv')
    image_dir = 'img_align_celeba'

    # initialize the graph
    celeb_graph = CelebrityGraph()

    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Celeb Lookalike")

    # example
    user_input = {
        'Bald': False,
        'Eyeglasses': False,
        'Male': True,
        # etc
    }

    # add user as a node in the graph
    celeb_graph.add_node('user')

    # find lookalikes
    lookalikes = find_lookalikes(user_input, celeb_attributes, celeb_graph)

    # load the first matchs image for display
    if lookalikes:
        first_match = lookalikes[0][0]
        img_path = os.path.join(image_dir, first_match)
        image = load_image(img_path)
    else:
        image = None

    # GUI loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # White background

        # display the image on the screen if it exists
        if image:
            screen.blit(image, (300, 200))  # image position on screen

        pygame.display.flip()  # update the display

    pygame.quit()


if __name__ == "__main__":
    main()
