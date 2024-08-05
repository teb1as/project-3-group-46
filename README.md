#Project 3 - Celeb Lookalike

##Description: 

Our application compares information inputted by the user to a large database of celebrity faces and attribute 
information to find celebrities that look similar. For storing and utilizing the data, we used two data structures: a 
graph and a hashtable. The GUI is built using the tkinter library. We chose to use a graph because it allows for weights
between nodes, which is useful for showing similarities between the user and other celebrities. The hashtable is useful 
for storing the celebrity data, as it allows for quick lookups.

##Use: 

After running main.py, a gui is opened where the user inputs data about their physical 
features. The user can select options from various dropdown menus corresponding to different attributes such as 
hairstyle, hair color, facial hair, accessories, and additional features. Once the user has selected their attributes, 
they can click the "Find Lookalike" button to see the celebrity that looks the most similar to them.

##Features:
- Graph Data Structure: Utilizes a graph to store relationships and similarities between users and celebrities.
- Hashtable for Quick Lookups: Stores celebrity attributes for efficient data retrieval.
- User-Friendly GUI: Built with tkinter, providing an intuitive interface for users to input their physical features.
- Image Display: Shows the image of the celebrity that looks similar to the user.

##Credits:
    
    |Name         |Github User|

    |Tavian Douge |teb1as     |
    |Dylan Everett|Dylan E    |
    |Mark Cortez  |mark-cortez|
