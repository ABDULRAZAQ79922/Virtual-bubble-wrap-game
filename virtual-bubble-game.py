import tkinter as tk
import random


root = tk.Tk()
root.title("Cute Bubble Wrap Game")


bubble_size = 50
num_bubbles = 30
popped_bubbles = []


canvas = tk.Canvas(root, width=1440, height=600, bg="lightyellow")
canvas.pack()

pop_count_label = tk.Label(root, text="Popped Bubbles: 0", font=("Helvetica", 14), bg="lightblue")
pop_count_label.pack()


def update_pop_count():
    pop_count_label.config(text=f"Popped Bubbles: {len(popped_bubbles)}")


def create_bubble(x, y):
    color = random.choice(["pink", "lightgreen", "lightblue", "lavender"])
    bubble = canvas.create_oval(x, y, x + bubble_size, y + bubble_size, fill=color, outline="")
    canvas.tag_bind(bubble, "<Button-1>", lambda event: pop_bubble(bubble))
    return bubble


def pop_bubble(bubble):
    if bubble not in popped_bubbles:
        popped_bubbles.append(bubble)
        canvas.itemconfig(bubble, fill="white", outline="white")
        canvas.create_text(canvas.coords(bubble)[0] + bubble_size/2, canvas.coords(bubble)[1] + bubble_size/2, text="Pop!", font=("Helvetica", 10), fill="black")
        update_pop_count()


def reset_game():
    global popped_bubbles
    popped_bubbles = []
    canvas.delete("all")
    update_pop_count()
    create_initial_bubbles()


def create_initial_bubbles():
    bubbles = []
    for _ in range(num_bubbles):
        x = random.randint(0, 550)
        y = random.randint(0, 350)
        bubble = create_bubble(x, y)
        bubbles.append(bubble)


restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12), command=reset_game)
restart_button.pack()


create_initial_bubbles()


root.mainloop()
