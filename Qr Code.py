from tkinter import *
from tkinter.ttk import *
import qrcode
import cv2

root = Tk()

#Window
root.geometry("700x500")
root.title("QR CODE")

def qr_generator():
    global Image
    data = qr_data.get()
    qr = qrcode.QRCode(version = 1, box_size = 6, border = 4)
    qr.add_data(data)
    qr.make(fit = True)

    name = qr_name.get()+".png"

    qr_img = qr.make_image(fill_color= "black", back_color ="white")

    qr_img.save(f'.\pics\{name}')

    Image = PhotoImage(file=f'.\pics\{name}')
    qr_img_lab.config(image=Image)

s = Style()
s.configure("TFrame", background="black", foreground= "white",padx= 50)
note = Notebook(root,style="TFrame")
tab1 = Frame(note,style="TFrame")
tab2 = Frame(note,style="TFrame")
note.add(tab1, text='QR CODE GENERATOR')
note.add(tab2, text="QR CODE DECODER")
note.pack(fill=BOTH)

can1 = Canvas(tab1, width=500,height=480,borderwidth=4,relief=SOLID)
can1.pack()
qr_img_lab = Label(root,borderwidth=2,relief=SOLID)

can1.create_window(250,150,window=qr_img_lab)

qr_name = Entry(root)
qr_data = Entry(root)
btn = Button(root,command=qr_generator)
can1.create_window(250,300,window=qr_data)
can1.create_window(250,350,window=qr_name)
can1.create_window(250,400,window=btn)

# lab = Label(root)
# lab.pack()

root.mainloop()