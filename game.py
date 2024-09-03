import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, comp_choice)
    update_score(result)
    update_labels(user_choice, comp_choice, result)

def determine_winner(user, comp):
    if user == comp:
        return "Tie"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "User"
    else:
        return "Comp"

def update_score(result):
    global user_score, comp_score
    if result == "User":
        user_score += 1
    elif result == "Comp":
        comp_score += 1

def update_labels(user_choice, comp_choice, result):
    user_label.config(text=f"User Choice: {user_choice}")
    comp_label.config(text=f"Comp Choice: {comp_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score - User: {user_score} Comp: {comp_score}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stone Paper Scissors")

    user_score = 0
    comp_score = 0

    tk.Label(root, text="Choose your move:").pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    tk.Button(button_frame, text="Rock", command=lambda: play("Rock")).pack(side=tk.LEFT)
    tk.Button(button_frame, text="Paper", command=lambda: play("Paper")).pack(side=tk.LEFT)
    tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors")).pack(side=tk.LEFT)

    user_label = tk.Label(root, text="User Choice: ")
    user_label.pack()

    comp_label = tk.Label(root, text="Comp Choice: ")
    comp_label.pack()

    result_label = tk.Label(root, text="Result: ")
    result_label.pack()

    score_label = tk.Label(root, text="Score - User: 0 Comp: 0")
    score_label.pack()

    root.mainloop()