import subprocess
import sys

# Function to install a package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure required packages are installed
try:
    from PIL import Image, ImageDraw, ImageTk
except ImportError:
    install_package('Pillow')
    from PIL import Image, ImageDraw, ImageTk

try:
    import pygame
except ImportError:
    install_package('pygame')
    import pygame

import tkinter as tk

class JoystickBarDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("Joystick Axis Display")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)
        
        # Initialize pygame for joystick handling
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() == 0:
            print("No joystick connected")
            pygame.quit()
            sys.exit()
        
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        # Create canvas for drawing bars
        self.canvas_width = 230  # Increased width to provide space for labels
        self.canvas_height = 320  # Increased height for margin
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.bar_width = 50
        self.axis_0_bar = self.canvas.create_rectangle(70, 10, 70 + self.bar_width, self.canvas_height - 10, fill="red")
        self.axis_1_bar = self.canvas.create_rectangle(150, 10, 150 + self.bar_width, self.canvas_height - 10, fill="red")

        # Draw y-axis
        self.draw_y_axis()

        self.update_bars()

    def draw_y_axis(self):
        # Draw the y-axis line
        self.canvas.create_line(40, 10, 40, self.canvas_height - 10, fill="black")

        # Draw y-axis labels from 0 to 1 with margin
        for i in range(11):
            y = self.canvas_height - 10 - (i / 10) * (self.canvas_height - 20)
            self.canvas.create_text(30, y, text=f"{i / 10:.1f}", anchor="e")

    def update_bars(self):
        pygame.event.pump()
        axis_0_value = self.joystick.get_axis(1)  # X axis (left/right)
        axis_1_value = self.joystick.get_axis(3)  # Y axis (up/down)

        # Normalize values from -1.0 - 1.0 to 0 - 1.0
        axis_0_normalized = (axis_0_value + 1) / 2.0
        axis_1_normalized = (axis_1_value + 1) / 2.0

        # Convert normalized values to canvas height
        axis_0_height = int(axis_0_normalized * (self.canvas_height - 20))
        axis_1_height = int(axis_1_normalized * (self.canvas_height - 20))

        self.canvas.coords(self.axis_0_bar, 70, self.canvas_height - 10 - axis_0_height, 70 + self.bar_width, self.canvas_height - 10)
        self.canvas.coords(self.axis_1_bar, 150, self.canvas_height - 10 - axis_1_height, 150 + self.bar_width, self.canvas_height - 10)

        self.root.after(50, self.update_bars)

if __name__ == "__main__":
    root = tk.Tk()
    app = JoystickBarDisplay(root)
    root.mainloop()
