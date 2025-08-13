import tkinter as tk
from PIL import Image, ImageTk
import random

# Create main window
win = tk.Tk()
win.title("Dice Roller")
win.geometry("300x300")

# Load dice images (Make sure they are in the same folder as this script)
dice_images =  [ImageTk.PhotoImage(Image.open(f"dice{i}.png").resize((100, 100)))
                for i in range(1, 7) ]


# Function to roll dice
def roll_dice():
    num = random.randint(1, 6)
    dice_label.config(image=dice_images[num - 1])
    result_label.config(text=f"You rolled: {num}")

# Dice label (default image: dice1)
dice_label = tk.Label(win, image=dice_images[0])
dice_label.pack(pady=20)

# Result label
result_label = tk.Label(win, text="Click below to roll!", font=("Arial", 14))
result_label.pack()

# Roll button
tk.Button(win, text="Roll Dice", command=roll_dice, font=("Times New Roman", 12), bg="blue", fg="white").pack(pady=20)

win.mainloop()

