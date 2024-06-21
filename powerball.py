import random
import time
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

# Powerball constants
WHITE_BALLS = 69
RED_BALLS = 26

# Function to draw balls
def draw_balls():
    white_balls = random.sample(range(1, WHITE_BALLS + 1), 5)
    red_ball = random.randint(1, RED_BALLS)
    return sorted(white_balls), red_ball

# Function to animate ball selection
def animate_ball_selection():
    start_button.config(state=tk.DISABLED)  
    
    balls = draw_balls()
    white_balls, red_ball = balls
    
    for i in range(5):
        canvas.delete(f"white_ball_{i}") 
        canvas.create_oval(50 + i * 100, 100, 100 + i * 100, 150, fill="white", tags=f"white_ball_{i}")
        canvas.create_text(75 + i * 100, 125, text=str(white_balls[i]), font=("Arial", 16), fill="black", tags=f"white_ball_{i}")
        canvas.update()
        time.sleep(1)
    
    canvas.delete("red_ball") 
    canvas.create_oval(350, 200, 400, 250, fill="red", tags="red_ball")
    canvas.create_text(375, 225, text=str(red_ball), font=("Arial", 16), fill="white", tags="red_ball")
    canvas.update()
    
    new_game_button.place(x=250, y=300)  # Show the "New Game" button

# Function to start a new game
def start_new_game():
    canvas.delete("all")  
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)  
    new_game_button.place_forget()  # Hide the "New Game" button
    start_button.config(state=tk.NORMAL)  # Enable the "Start Game" button

# Create the main window
window = tk.Tk()
window.title("Powerball Simulator")
window.geometry("600x400")

# Load the background image
background_image_path = "powerbackground.png"
background_image = ImageTk.PhotoImage(Image.open(background_image_path).resize((600, 400)))

# Create a canvas for drawing the balls and background
canvas = Canvas(window, width=600, height=400)
canvas.pack()

# Set the initial background
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Create a button to start the animation
start_button = tk.Button(window, text="Start Game", font=("Arial", 16), command=animate_ball_selection)
start_button.place(x=250, y=300)

# Create a button to start a new game
new_game_button = tk.Button(window, text="New Game", font=("Arial", 16), command=start_new_game)

# Start the GUI event loop
window.mainloop()