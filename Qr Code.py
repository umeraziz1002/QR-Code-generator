from tkinter import *
import qrcode
import cv2


root = Tk()

#Window
root.geometry("700x500")
root.title("QR CODE")

data = "my name is Umer"

qr = qrcode.QRCode(version = 1, box_size = 6, border = 4)
qr.add_data(data)
qr.make(fit = True)
name = "check.png"

qr_img = qr.make_image(fill_color= "black", back_color ="white")

qr_img.save(name)

lab = Label(root)
lab.pack()

Image = PhotoImage(file=f'{name}')

lab.config(image=Image)


root.mainloop()