import tkinter as tk
import random

root = tk.Tk()
root.title("3D Dice Game")
root.geometry("400x500")
root.config(bg="#f0f8ff")  # Light blue main window background

DICE_SIZE = 80
DICE_COLORS = ["lightblue", "lightgreen", "lightcoral"]
DICE_SHADOW_COLOR = "grey"
DOT_COLOR = "black"

def draw_dice(canvas, value, dice_color):
    canvas.delete("all")
    shadow_x, shadow_y = 10, 10
    canvas.create_rectangle(
        shadow_x, shadow_y, shadow_x + DICE_SIZE, shadow_y + DICE_SIZE,
        fill=DICE_SHADOW_COLOR, outline=""
    )
    canvas.create_rectangle(
        0, 0, DICE_SIZE, DICE_SIZE,
        fill=dice_color, outline="black", width=2
    )
    dot_positions = {
        1: [(DICE_SIZE // 2, DICE_SIZE // 2)],
        2: [(DICE_SIZE // 4, DICE_SIZE // 4), (3 * DICE_SIZE // 4, 3 * DICE_SIZE // 4)],
        3: [(DICE_SIZE // 4, DICE_SIZE // 4), (DICE_SIZE // 2, DICE_SIZE // 2), (3 * DICE_SIZE // 4, 3 * DICE_SIZE // 4)],
        4: [(DICE_SIZE // 4, DICE_SIZE // 4), (3 * DICE_SIZE // 4, DICE_SIZE // 4), (DICE_SIZE // 4, 3 * DICE_SIZE // 4), (3 * DICE_SIZE // 4, 3 * DICE_SIZE // 4)],
        5: [(DICE_SIZE // 4, DICE_SIZE // 4), (3 * DICE_SIZE // 4, DICE_SIZE // 4), (DICE_SIZE // 2, DICE_SIZE // 2), (DICE_SIZE // 4, 3 * DICE_SIZE // 4), (3 * DICE_SIZE // 4, 3 * DICE_SIZE // 4)],
        6: [(DICE_SIZE // 4, DICE_SIZE // 4), (3 * DICE_SIZE // 4, DICE_SIZE // 4), (DICE_SIZE // 4, DICE_SIZE // 2), (3 * DICE_SIZE // 4, DICE_SIZE // 2), (DICE_SIZE // 4, 3 * DICE_SIZE // 4), (3 * DICE_SIZE // 4, 3 * DICE_SIZE // 4)],
    }
    for pos in dot_positions[value]:
        canvas.create_oval(
            pos[0] - 5, pos[1] - 5, pos[0] + 5, pos[1] + 5,
            fill=DOT_COLOR
        )

def roll_all_dice():
    total = 0
    for i, canvas in enumerate(dice_canvases):
        dice_value = random.randint(1, 6)
        draw_dice(canvas, dice_value, DICE_COLORS[i])
        total += dice_value
    result_label.config(text=f"Total: {total}")  # Update the result label with the sum

def reset_all_dice():
    for i, canvas in enumerate(dice_canvases):
        draw_dice(canvas, 1, DICE_COLORS[i])
    result_label.config(text="Total: 3")  # Reset the result label to 3 (1+1+1)

# Create a central frame for the game with a different background color
game_frame = tk.Frame(root, bg="#e6e6fa", width=350, height=450)  # Light lavender
game_frame.place(relx=0.5, rely=0.5, anchor="center")

# Place the dice canvases inside the game frame
dice_canvases = [
    tk.Canvas(game_frame, width=DICE_SIZE + 20, height=DICE_SIZE + 20, bg="white", highlightthickness=0)
    for _ in range(3)
]
for i, canvas in enumerate(dice_canvases):
    canvas.place(x=35 + i * 110, y=100)

# Create a label to display the result sum in a red box
result_label = tk.Label(game_frame, text="Total: 3", font=("Arial", 16), bg="red", fg="white", width=15, height=2)
result_label.place(x=90, y=200)

# Create 3D styled buttons
button_style = {"font": ("Arial", 16), "relief": "raised", "bd": 5, "padx": 10, "pady": 5}

roll_button = tk.Button(game_frame, text="Roll Dice", command=roll_all_dice, bg="blue", fg="white", **button_style)
roll_button.place(x=90, y=300)

reset_button = tk.Button(game_frame, text="Reset", command=reset_all_dice, bg="red", fg="white", **button_style)
reset_button.place(x=90, y=350)

# Initialize the dice to value 1
reset_all_dice()
root.mainloop()
