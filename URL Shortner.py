from tkinter import *
from tkinter import font
import pyshorteners # type: ignore
import pyperclip # type: ignore

#Method for shortning
def shorten_url():
    sort_Url = url.get()
    generatedurl = pyshorteners.Shortener().tinyurl.short(sort_Url) #short the main url and store 
    sortUrl.set(generatedurl)  #set into the sortUrl
    
def copy(button):
    generatedurl = sortUrl.get()  #get sortUrl store into generatedurl
    pyperclip.copy(generatedurl)  #copy that
    button.config(text="Copied",width=15, font=button_font)

#GUI Setup
root = Tk()
root.title("URL SHORTNER")
root.configure(bg= "lightgrey")

url = StringVar()  #store main url
sortUrl = StringVar() #store short url

button_font = font.Font(size=10,weight='bold')

label = Label(root,text = "Enter URL : ",  bg="green", fg="white",width=20, font=button_font).pack(pady = 10)  #first label
Entry(root, textvariable =url, width=50).pack(pady =5)  #input Box

Button(root, text = "Shorten URL", command=shorten_url, bg="green", fg="white", width=20, font=button_font).pack(pady=5)
Entry(root, textvariable=sortUrl, width=50).pack(pady=5)

copy_button = Button(root, text="Copy URL", command=lambda: copy(copy_button), width=15, font=button_font)
copy_button.pack(pady=5)


root.mainloop()