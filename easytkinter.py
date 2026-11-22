import tkinter as tk



#Window atributes--------------

def window(x = 400, y = 300, text = "ETK window"):
    global root
    root = tk.Tk()
    root.geometry(f"{x}x{y}")
    root.title(text)

def geometry(x, y):
    root.geometry(f"{x}x{y}")

def title(text):
    root.title(text)

#Widgets----------------------

def rlabel(text="", 
            font=None, 
            fg=None, 
            bg=None, 
            padx=1, 
            pady=1):
    
    label = tk.Label(root, 
                    text=text, 
                    font=font, 
                    fg=fg, 
                    bg=bg, 
                    padx=padx, 
                    pady=pady)
    label.pack()
    return label

def rbutton(text="", 
            command=None, 
            bg=None, 
            fg=None, 
            font=None, 
            state="normal", 
            width=None, 
            height=None,
            activebackground=None,
            activeforeground=None):
    button = tk.Button(root, 
                    text=text, 
                    font=font, 
                    command=command,
                    fg=fg, 
                    bg=bg, 
                    state=state, 
                    width=width,
                    height=height,
                    activebackground=activebackground,
                    activeforeground=activeforeground)
    button.pack()
    return button



def rcheckbtn(text="", 
            variable=None, 
            onvalue=None,
            offvalue=None, 
            command=None):
    checkbutton = tk.Checkbutton(text=text, 
                                variable=variable, 
                                onvalue=onvalue, 
                                offvalue=offvalue, 
                                command=command)
    checkbutton.pack()
    return checkbutton

def rradiobtn(text="", 
            variable=None, 
            value=None, 
            command=None, 
            state=None):
    radiobutton = tk.Radiobutton(text=text, 
                                variable=variable, 
                                value=value, 
                                command=command, 
                                state=state)
    radiobutton.pack()
    return radiobutton




#Variables--------------------    

def boolvar(value=None):
    varbool = tk.BooleanVar(value=value)
    return varbool

def strvar(value=""):
    varstr = tk.StringVar(value=value)
    return varstr

#Mainloop----------------------

def run():
    root.mainloop()


