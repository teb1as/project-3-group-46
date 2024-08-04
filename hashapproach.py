import csv
import pygame
from PIL import Image
import os

# HashMap: storing celebrity attributes
def load_attributes(file_path):
    celebrity_attributes = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            celeb_id = row['image_id']
            attributes = {key: (value == '1') for key, value in row.items() if key != 'image_id'}
            celebrity_attributes[celeb_id] = attributes
    return celebrity_attributes

# calculate similarity
def calculate_similarity(user_features, celeb_features):
    score = 0
    for feature, value in user_features.items():
        if celeb_features.get(feature) == value:
            score += 1
    return score

# find lookalikes based on similarity using a hashtable approach
def find_lookalikes(user_features, celebrity_attributes):
    lookalikes = []
    for celeb_id, celeb_features in celebrity_attributes.items():
        similarity = calculate_similarity(user_features, celeb_features)
        lookalikes.append((celeb_id, similarity))
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

    # find lookalikes
    lookalikes = find_lookalikes(user_input, celeb_attributes)

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