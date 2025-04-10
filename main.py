from tkinter import *

BLACK = "#323232"
GREY = "#555555"

window = Tk()

window.title("Personal Expense Tracker")
window.config(bg=BLACK)

outer_frame = Frame(window, bg=BLACK, padx=20, pady=20)
outer_frame.grid(row=1, column=0, padx=20, pady=20)
label = Label(window, text="Personal Expense Tracker", font="Arial")
label.grid(column=0, row=1)

canvas = Canvas(outer_frame, height=500, width=500, bg=GREY, highlightthickness=0)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(250, 250, image=logo_img)  # centered in 300x300
canvas.grid()


###################################buttons########################################
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text=new_text)

button = Button(text="Add Expense", command=button_clicked)
button.grid(column=0, row=3, sticky="e", padx=40)
new_button = Button(text="Expense History")
new_button.grid(column=0, row=4, sticky="e", padx=40)

########################Inputs###########################
input = Entry(width=25)
print(input.get())
input.grid(column=0, row=3)

window.mainloop()