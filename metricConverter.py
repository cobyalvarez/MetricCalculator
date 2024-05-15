import tkinter as tk

#-----------------------------------------------conversion values and function
def convert(): 
    input_value = float(entry.get())
    # print(input_value)
    initial = original_val.get()
    final = convert_to.get()

    conversion = {
        ("Miles","Kilometers"): 1.60934,
        ("Kilometers","Miles"): 0.621371,
        ("Pounds","Kilograms"): 0.453592,
        ("Kilograms","Pounds"): 2.20462,
        ("Inches","Centimeters"): 2.54,
        ("Centimeters","Inches"): 0.393701
    }

    result_val = input_value * conversion[initial,final]

    result.config(text=f"{result_val:.2f} {final}")

#------------------------------------------------the action occurres when the button is pressed
# def show(): 
#     print("clicked") 
  
#create the main window 
window = tk.Tk()
window.title("Unit Conversion")

window.geometry("200x200")

input_label = tk.Label(text="Enter Value:", fg="black",bg="grey")
input_label.pack()
    
#create a input
entry = tk.Entry(window, width=10)
entry.pack()

#_______________________________________________________________#dropdown menu section
# Dropdown menu options 
options = [ 
    "Miles", 
    "Kilometers", 
    "Inches", 
    "Centimeters",
    "Kilograms",
    "Pounds"
    
] 
# Create a frame to hold the menus
dropdown_frame = tk.Frame(window)
dropdown_frame.pack()
  
# datatype of from text 
original_val = tk.StringVar() 
original_val.set( "Inital value" ) 
# Create Dropdown menu 
drop_original = tk.OptionMenu( dropdown_frame , original_val , *options ) 
drop_original.pack(side="left") 

# datatype of converstion to text 
convert_to = tk.StringVar() 
convert_to.set( "Result Value" ) 
# Create Dropdown menu 
drop_to = tk.OptionMenu( dropdown_frame , convert_to , *options ) 
drop_to.pack(side="right") 

#________________________________________________________#Button to convert
# Create convert button
Button = tk.Button(window, text='Convert', command = convert)
Button.pack()


# Create result label
value = tk.Label(text="Result:", fg="black",bg="white")
value.pack()
result = tk.Label(text="Result", fg="black",bg="grey")
result.pack()


# Start the GUI
window.mainloop()
