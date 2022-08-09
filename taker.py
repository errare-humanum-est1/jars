from Jarmanager import JarManager
import tkinter as tk

def displayEntry(entry):
    label.config(text=entry)    

jar = JarManager()
window = tk.Tk()
window.title("Taker")

greeting = tk.Label(text="Choose your Jar below:")
greeting.pack()

label = tk.Label(text="")
label.pack()

button_dict = {}

for daddy in jar.get_jar_keys():
    def func(x = daddy):
        displayEntry(jar.take_from_jar(x))
    
    button_dict[jar] = tk.Button(text=daddy, command= func)
    button_dict[jar].pack()

def qui():
    jar.write_file()
    exit()    

button_dict["exit"] = tk.Button(text="Exit", command=qui)
button_dict["exit"].pack()

window.mainloop()