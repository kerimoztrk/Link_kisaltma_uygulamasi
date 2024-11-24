import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip


def shortenUrl():
    longUrl=entry.get()
    response= requests.get(f'http://tinyurl.com/api-create.php?url={longUrl}')
    shortUrl=response.text
    resultLabel.config(text=f'Kısaltılmış link : {shortUrl}')
    copyButton.config(state=tk.NORMAL)

def copyToClipboard():
    shortUrl=resultLabel.cget("text")[18:]
    pyperclip.copy(shortUrl)
    messagebox.showinfo("kopyalandı","Kısa URL KOPYALANDI")

root=tk.Tk()
root.title("Link Kısaltıcı")

label=tk.Label(root,text="uzun linki giriniz.")
label.pack()
entry=tk.Entry(root,width=40)
entry.pack()
shortenButton=tk.Button(text="Kısalt",command=shortenUrl)
shortenButton.pack()

resultLabel=tk.Label(root,text="")
resultLabel.pack()

copyButton=tk.Button(root,text="Kopyala",command=copyToClipboard,state=tk.DISABLED)
copyButton.pack()

root.mainloop()