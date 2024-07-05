import subprocess
import sys

# Function to install a package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure required packages are installed
try:
    from PIL import Image, ImageTk
except ImportError:
    install_package('Pillow')
    from PIL import Image, ImageTk

try:
    import keyboard
except ImportError:
    install_package('keyboard')
    import keyboard

import tkinter as tk
import os

class NumberKeyDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Key Display")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)

        # Determine the current working directory
        current_dir = os.getcwd()

        # Path to the image folder
        image_folder = os.path.join(current_dir, 'numberkeys_images')

        # Initialize image dictionaries
        self.unpressed_images = {}
        self.pressed_images = {}

        # Load and resize images
        for i in range(1, 11):
            number = i % 10
            unpressed_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, f"number{number}_unpressed.png")).resize((50, 50), Image.Resampling.LANCZOS))
            pressed_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, f"number{number}_pressed.png")).resize((50, 50), Image.Resampling.LANCZOS))
            self.unpressed_images[number] = unpressed_image
            self.pressed_images[number] = pressed_image

        # Setup labels for each number key
        self.labels = {}
        for i in range(10):
            number = (i + 1) % 10
            label = tk.Label(root, image=self.unpressed_images[number])
            label.grid(row=0, column=i)
            self.labels[number] = label

        self.update_images()

    def update_images(self):
        for i in range(10):
            number = (i + 1) % 10
            if keyboard.is_pressed(str(number)):
                self.labels[number].config(image=self.pressed_images[number])
            else:
                self.labels[number].config(image=self.unpressed_images[number])

        self.root.after(50, self.update_images)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberKeyDisplay(root)
    root.mainloop()
