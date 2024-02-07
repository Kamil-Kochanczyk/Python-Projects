import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import random

WIDTH, HEIGHT = 600, 400
ROCK, PAPER, SCISSORS = "Rock", "Paper", "Scissors"
WINS_WITH, TIES_WITH, LOSES_WITH = "wins_with", "ties_with", "loses_with"
PLAYER_WINS, ITS_A_TIE, COMPUTER_WINS = "Player wins!", "It's a tie!", "Computer wins!"
MAX_POINTS = 3
YOU_WON, YOU_LOST = "You won!", "You lost!"

root = tk.Tk()
root.geometry(str(WIDTH) + "x" + str(HEIGHT))
root.resizable(width=False, height=False)
root.title("Rock, Paper, Scissors")

player_score = tk.IntVar()
computer_score = tk.IntVar()
player_choice = tk.StringVar()
computer_choice = tk.StringVar()
result = tk.StringVar()

rock_dict = {WINS_WITH: SCISSORS, TIES_WITH: ROCK, LOSES_WITH: PAPER}
paper_dict = {WINS_WITH: ROCK, TIES_WITH: PAPER, LOSES_WITH: SCISSORS}
scissors_dict = {WINS_WITH: PAPER, TIES_WITH: SCISSORS, LOSES_WITH: ROCK}

choices = {ROCK: rock_dict, PAPER: paper_dict, SCISSORS: scissors_dict}

def handle_player_choice(choice):
    global player_score
    global computer_score
    global player_choice
    global computer_choice
    global result
    
    player_choice.set(choice)
    computer_choice.set(random.choice([ROCK, PAPER, SCISSORS]))

    if choices[player_choice.get()][WINS_WITH] == computer_choice.get():
        player_score.set(player_score.get() + 1)
        result.set(PLAYER_WINS)
    
    if choices[player_choice.get()][TIES_WITH] == computer_choice.get():
        result.set(ITS_A_TIE)
    
    if choices[player_choice.get()][LOSES_WITH] == computer_choice.get():
        computer_score.set(computer_score.get() + 1)
        result.set(COMPUTER_WINS)
    
    if player_score.get() == MAX_POINTS or computer_score.get() == MAX_POINTS:
        play_again = -1

        if player_score.get() == MAX_POINTS:
            play_again = show_message_box(YOU_WON)

        if computer_score.get() == MAX_POINTS:
            play_again = show_message_box(YOU_LOST)    

        if play_again == 1:
            player_score.set(0)
            computer_score.set(0)
            player_choice.set("")
            computer_choice.set("")
            result.set("")
        else:
            root.destroy()

def show_message_box(message):
    return messagebox.askyesno("Game Over", message + " Do you want to play again?")

custom_font = font.Font(family="Helvetica", size=12)
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=(10, 5))

user_frame = tk.LabelFrame(root)
computer_frame = tk.LabelFrame(root)
result_frame = tk.LabelFrame(root)

for i in range(4):
    user_frame.rowconfigure(i, minsize = (0.75 * HEIGHT) / 4)
user_frame.columnconfigure(0, minsize = WIDTH / 2)

for i in range(4):
    computer_frame.rowconfigure(i, minsize = (0.75 * HEIGHT) / 4)
computer_frame.columnconfigure(0, minsize = WIDTH / 2)

result_frame.rowconfigure(0, minsize = HEIGHT / 4)
for i in range(3):
    result_frame.columnconfigure(i, minsize = WIDTH / 3)

user_frame.grid(row=0, column=0)
computer_frame.grid(row=0, column=1)
result_frame.grid(row=1, column=0, columnspan=2)

player_score_lbl = tk.Label(user_frame, textvariable=player_score, font=custom_font)
player_rock_btn = ttk.Button(user_frame, text=ROCK, command=lambda: handle_player_choice(ROCK))
player_paper_btn = ttk.Button(user_frame, text=PAPER, command=lambda: handle_player_choice(PAPER))
player_scissors_btn = ttk.Button(user_frame, text=SCISSORS, command=lambda: handle_player_choice(SCISSORS))

player_score_lbl.grid(row=0, column=0)
player_rock_btn.grid(row=1, column=0)
player_paper_btn.grid(row=2, column=0)
player_scissors_btn.grid(row=3, column=0)

computer_score_lbl = tk.Label(computer_frame, textvariable=computer_score, font=custom_font)
computer_rock_btn = ttk.Button(computer_frame, text=ROCK, state="disabled")
computer_paper_btn = ttk.Button(computer_frame, text=PAPER, state="disabled")
computer_scissors_btn = ttk.Button(computer_frame, text=SCISSORS, state="disabled")

computer_score_lbl.grid(row=0, column=0)
computer_rock_btn.grid(row=1, column=0)
computer_paper_btn.grid(row=2, column=0)
computer_scissors_btn.grid(row=3, column=0)

player_choice_lbl = tk.Label(result_frame, textvariable=player_choice, font=custom_font)
computer_choice_lbl = tk.Label(result_frame, textvariable=computer_choice, font=custom_font)
result_lbl = tk.Label(result_frame, textvariable=result, font=custom_font)

player_choice_lbl.grid(row=0, column=0)
computer_choice_lbl.grid(row=0, column=2)
result_lbl.grid(row=0, column=1)

root.mainloop()
