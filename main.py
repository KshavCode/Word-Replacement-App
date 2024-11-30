from tkinter import *
import tkinter.messagebox as tmb
import pyperclip as pc

root = Tk()
root.geometry("700x400")
root.title("Word Replacement App")
root.resizable(False, False)
changed_text = ""

def paste_text():
    try:
        clipboard_content = root.clipboard_get() 
        entry1.insert(INSERT, clipboard_content)  
    except :
        tmb.showerror("ERROR", "Unsupported content in the clipboard. Make sure it is in text format!")

def replacement()->str :
    global changed_text
    entry1_value = str(entry1.get("1.0", END))
    entry1_value = entry1_value.replace("no", "yes")
    changed_text = entry1_value
    label2.config(text=entry1_value)
    button2 = Button(root, text="Copy to Clipboard", font="arial 14", wraplength=100, width=10, bg="lightblue", command=clip)
    button2.place(x=550, y=120)

def clip()->None :
    global changed_text
    try :
        pc.copy(changed_text)
        tmb.showinfo("SUCCESS", "Text has been copied to the clipboard.")
    except Exception as e:
        tmb.showerror(f"ERROR", "Problem with accessing clipboard! ({e})")

label1 = Label(root, text="Your Text Here : ", font="arial 14")
entry1 = Text(root, font="arial 13", width=55)
label2 = Label(root, text="", font="arial 13", wraplength=500, justify=LEFT)
button1 = Button(root, text="Start Replacing", font="arial 14", wraplength=100, width=10, bg="lightgreen", command=replacement)


label1.place(x=10, y=10)
entry1.place(x=10, y=40, height=150)
label2.place(x=10, y=200)
button1.place(x=550, y=50)

root.mainloop()