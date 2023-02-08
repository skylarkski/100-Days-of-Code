from tkinter import * 

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

def calculate():
    miles_to_km = str(round(float(entry_miles.get()) * 1.609 ,2))
    calculated_km.config(text=miles_to_km)


#Entry
entry_miles = Entry(width=10)
entry_miles.grid(column=1, row=0)


#Label miles
label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)


#Label km
label_km = Label(text="Kilometers")
label_km.grid(column=2,row=1)


#Label is equal to
equal_to = Label(text="is equal to")
equal_to.grid(column=0,row=1)


#Km answer
calculated_km = Label(text="0")
calculated_km.grid(column=1,row=1)


#Button calculate
button_calc = Button(text="Calculate", command=calculate)
button_calc.grid(column=1,row=3)






window.mainloop()