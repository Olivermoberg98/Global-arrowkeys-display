import tkinter as tk
from PIL import Image, ImageTk
import keyboard
import os

class ArrowKeyDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("Arrow Key Display")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)

        # Path to the image folder
        image_folder = 'Global-arrowkeys-display/arrowkey_images'

        # Load and resize images
        self.left_unpressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "left_unpressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.left_pressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "left_pressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.right_unpressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "right_unpressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.right_pressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "right_pressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.up_unpressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "up_unpressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.up_pressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "up_pressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.down_unpressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "down_unpressed.png")).resize((100, 100), Image.Resampling.LANCZOS))
        self.down_pressed = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "down_pressed.png")).resize((100, 100), Image.Resampling.LANCZOS))

        # Setup labels
        self.left_label = tk.Label(root, image=self.left_unpressed)
        self.left_label.grid(row=1, column=0)
        self.up_label = tk.Label(root, image=self.up_unpressed)
        self.up_label.grid(row=0, column=1)
        self.down_label = tk.Label(root, image=self.down_unpressed)
        self.down_label.grid(row=1, column=1)
        self.right_label = tk.Label(root, image=self.right_unpressed)
        self.right_label.grid(row=1, column=2)

        self.update_images()

    def update_images(self):
        if keyboard.is_pressed('left'):
            self.left_label.config(image=self.left_pressed)
        else:
            self.left_label.config(image=self.left_unpressed)

        if keyboard.is_pressed('right'):
            self.right_label.config(image=self.right_pressed)
        else:
            self.right_label.config(image=self.right_unpressed)

        if keyboard.is_pressed('up'):
            self.up_label.config(image=self.up_pressed)
        else:
            self.up_label.config(image=self.up_unpressed)

        if keyboard.is_pressed('down'):
            self.down_label.config(image=self.down_pressed)
        else:
            self.down_label.config(image=self.down_unpressed)

        self.root.after(50, self.update_images)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArrowKeyDisplay(root)
    root.mainloop()
