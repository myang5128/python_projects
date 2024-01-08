from tkinter import *

window = Tk()
window.title("Practice GUI")
window.minsize(width=500, height=300)

def button_Click():
    input_Result = input.get()
    print(input_Result)

label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "New Text"
label.config(text="New Text")

button = Button(text="Click Me", command=button_Click)
button.pack()

input = Entry(width=10)
input.pack()


window.mainloop()