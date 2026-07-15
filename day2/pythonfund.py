from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("sabocode")
window.configure(bg="red")

# persistent counter
count = 0

def clikhere():
    global count
    count += 1
    if count > 3:
        button.config(text=f"stop clik me please")
    else:
        button.config(text=f" {count} likes")
    # update button text to show clicks
def subscribe():
    buttonsub.config(text="subscribed")
    buttonsub.config(fg="yellow")
button = Button(window,
                text="Click me please",
                fg="white",
                command=clikhere,
                font=("Arial", 16),
                bg="black")
button.pack(pady=20)
buttonsub=Button(window,
                 text="subscribe",
                 fg="white",
                 command=subscribe,
                 font=("Arial",16),
                 bg="black")
buttonsub.pack(pady=20)

window.mainloop()
