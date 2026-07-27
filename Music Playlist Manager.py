# ================================
# MY ART GALLERY COLLECTION MANAGER
# ================================

class ArtGallery:

    # Constructor with parameters
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location

        # Default attribute initialization
        self.artworks = []

        print(f"\nWelcome to {self.gallery_name}!")
        print(f"Location: {self.location}")
        print("Art gallery collection is ready.")

    # Class method to add an artwork
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' has been added to the gallery collection.")

    # Class method to remove an artwork
    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' has been removed from the gallery collection.")
        else:
            print(f"'{artwork}' was not found in the gallery collection.")

    # Class method to display all artworks
    def display_artworks(self):
        print(f"\n--- {self.gallery_name} Art Collection ---")

        if self.artworks:
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number}. {artwork}")
        else:
            print("No artworks have been added yet.")

    # Destructor
    def __del__(self):
        print(f"\nClosing {self.gallery_name}. Thank you for managing the art collection!")


# Object Lifecycle: object creation

gallery = ArtGallery("Creative Canvas Gallery", "Bengaluru")

# Menu-driven OOP program

while True:
    print("\n========= ART GALLERY MENU =========")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. Display Art Collection")
    print("4. Exit")
    print("===================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork_name = input("Enter the artwork name to add: ")
        gallery.add_artwork(artwork_name)

    elif choice == "2":
        artwork_name = input("Enter the artwork name to remove: ")
        gallery.remove_artwork(artwork_name)

    elif choice == "3":
        gallery.display_artworks()

    elif choice == "4":
        print("Exiting the Art Gallery Collection Manager.")

        # Object Lifecycle: object deletion
        del gallery
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
