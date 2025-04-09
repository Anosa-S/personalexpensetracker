from tkinter import *

BLACK = "#323232"
GREY = "#555555"

window = Tk()

window.title("Personal Expense Tracker")
window.config(bg=BLACK)
outer_frame = Frame(window, bg=BLACK, padx=20, pady=20)
outer_frame.grid(row=1, column=0, padx=20, pady=20)

canvas = Canvas(outer_frame, height=300, width=300, bg=GREY, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)  # centered in 300x300
canvas.pack()


###################################buttons########################################
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Add Expense", command=button_clicked)
button.grid(column=0, row=3)
new_button = Button(text="Expense History")
new_button.grid(column=0, row=4)
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)

window.mainloop()