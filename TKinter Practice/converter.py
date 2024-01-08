from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=25, pady=25)

def button_Click():
    input_Result = input.get()
    km = round(int(input_Result) * 1.609,2)
    result.config(text=f"{km}")
    
# first row
input = Entry(width=7)
input.grid(row=0, column=1)

miles_Label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_Label.grid(row=0, column=2)

# second row
equal_Label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_Label.grid(row=1, column=0)

result = Label(text="0", font=("Arial", 24, "bold"))
result.grid(row=1, column=1)

km_Label = Label(text="Km", font=("Arial", 24, "bold"))
km_Label.grid(row=1, column=2)

button = Button(text="Calculate", command=button_Click)
button.grid(row=2, column=1)


window.mainloop()