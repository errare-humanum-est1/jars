from Jarmanager import JarManager
import tkinter as tk

def Simpletoggle():    
    if toggle_button.config('text')[-1] == 'Entry':
        toggle_button.config(text='Jar')
    else:
        toggle_button.config(text='Entry')

def showJar():
    jar_val = list(jar.get_jar(ent_jar.get()))
    lbl_list_jar_contents.config(text=jar_val)
    
def add():
    jar_val = str(ent_jar.get())
    val_val = str(ent_val.get())
    if toggle_button.config('text')[-1] == 'Jar':
        jar.add_jar(jar_val)
        jar.add_entry(jar_val, val_val)
    else:
        jar.add_entry(jar_val, val_val)
    showJar()

def remove():
    jar_val = ent_jar.get()
    val_val = ent_val.get()
    if toggle_button.config('text')[-1] == 'Jar':
        jar.remove_jar(jar_val)
    else:
        jar.remove_entry(jar_val, val_val)
    showJar()


jar = JarManager()
window = tk.Tk()
window.title("Manage Jars")

# list all the jars
lbl_list_jars = tk.Label(text=f"Jars: {jar.get_jar_keys()}")
lbl_list_jars.pack()

# Label for toggle
lbl_btn_toggle = tk.Label(text="What do you want to add/remove?")
lbl_btn_toggle.pack(pady=10)

# toggle between jar and entry
toggle_button = tk.Button(text="Jar", width=10, command=Simpletoggle)
toggle_button.pack(pady=10)

# jar label for jar button
lbl_jar = tk.Label(text="Jar")
lbl_jar.pack()
# jar button
ent_jar = tk.Entry()
ent_jar.pack()

btn_list_jar = tk.Button(text="Show Jar Contents", command=showJar)
btn_list_jar.pack()

lbl_list_jar_contents = tk.Label(text="")
lbl_list_jar_contents.pack()


# val for val button
lbl_val = tk.Label(text="Value")
lbl_val.pack()
# jar button
ent_val = tk.Entry()
ent_val.pack()


# add button
addButton = tk.Button(text="Add", command=add)
addButton.pack()

# remove button
removeButton = tk.Button(text="Remove", command=remove)
removeButton.pack()


def qui():
    jar.write_file()
    exit()    

exitButton = tk.Button(text="Exit", command=qui)
exitButton.pack()

window.mainloop()