## Import Dialog
import tkinter.filedialog as tfd
## Import Tkinter messagebox
import tkinter.messagebox as tkm



# gui 
import tkinter as tk

#global filename
file_name = ""


# Functions
def openfile():
    content_text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    file_label["text"] = "File: "+file_name
    with open(file_name) as file:
        content_text.insert(1.0, file.read())

def saveas():
    global file_name
    file_name = tfd.asksaveasfilename()#Creating File
    file_label["text"] = "File: "+file_name
    content = content_text.get(1.0, "end") #Getting Content
    with open(file_name, "w") as file:
        file.write(content)

def new():
    global file_name
    if tkm.askokcancel("Creating New File", "Are you sure? Unsaved text will be deleted."):
        content_text.delete(1.0, "end")
        file_name = ""
        file_label["text"] = "File: "+file_name
    
    
def save():
    global file_name
    if file_name == "":
        saveas()
    else:
        content = content_text.get(1.0, "end")
        with open(file_name,"w") as file:
            file.write(content)
        tkm.showinfo("Saving File", "Saving Content to File: "+file_name)

        
        
    
window = tk.Tk()
window.title("Notepad")
window.geometry("1280x720")
content_text = tk.Text(window,bg = "gray39", fg = "snow")
content_text.place(x = 0, y = 0, relwidth = 1, relheight = 1)


## Menu
main_menu = tk.Menu(window)

window.configure(menu = main_menu)

file_label = tk.Label(window, text = "File:"+file_name)

file_menu = tk.Menu(main_menu, tearoff = 0)

# Buttons/ Cascades
main_menu.add_cascade(label = "File", menu = file_menu)

file_label.place(relx = 0, rely = 1, anchor = "sw")

newfile_icon = tk.PhotoImage(file = "Icons/new_file.gif")
file_menu.add_command(label = "New", image = newfile_icon, compound = "left", command = new)

openfile_icon = tk.PhotoImage(file = "Icons/open_file.gif")
file_menu.add_command(label = "Open", image = openfile_icon, compound = "left", command = openfile)

savefile_icon = tk.PhotoImage(file = "Icons/save_file.gif")
file_menu.add_command(label = "Save", image = savefile_icon, compound = "left", command = save)

saveasfile_icon = tk.PhotoImage(file = "Icons/save_file.gif")
file_menu.add_command(label = "Save As", image = savefile_icon, compound = "left", command = saveas)


##tkm.showinfo("Welcome!", "You are welcome to my application notepad.")

window.mainloop()


