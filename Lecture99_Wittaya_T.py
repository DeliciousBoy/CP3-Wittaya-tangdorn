from tkinter import *
import math

def leftclick(event):
    height = float(textbox_height.get())
    weight = float(textbox_weight.get())
    result = (weight/math.pow(height/100,2))
    if result > 30:
        label_result.configure(text="Fatty")
    elif result >= 25:
        label_result.configure(text="Plump")
    elif result >= 23:
        label_result.configure(text="Chubby")
    elif result >= 18.6:
        label_result.configure(text="Normal")
    elif result < 18.5:
        label_result.configure(text="Skinny")

main_window = Tk()
main_window.title("Calculate your BMI")

label_height = Label(main_window,text="Height (cm.)")
label_height.grid(row=0,column=0)
textbox_height = Entry(main_window)
textbox_height.grid(row=0,column=1)

label_weight = Label(main_window,text="Weight (kg.)")
label_weight.grid(row=1,column=0)
textbox_weight = Entry(main_window)
textbox_weight.grid(row=1,column=1)

calculate_button = Button(main_window,text = "Compute BMI")
calculate_button.bind("<Button-1>",leftclick)
calculate_button.grid(row=2)

label_result = Label(main_window,text="Result :")
label_result.grid(row=2,column=1)
main_window.mainloop()
