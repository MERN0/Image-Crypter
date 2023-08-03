from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('200x200')

#encrypting function
def encrypt_image():
    f=filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*jpg'), ('png file', '*.png')])
    if f:
        file_path=f.name
        key=entered_key.get(1.0, END)
        print(file_path, key)

        #reading_file_path
        read_fp=open(file_path, 'rb')
        image=read_fp.read()
        read_fp.close()

        #changing pixels in bytearrays
        image=bytearray(image)

        for index, values in enumerate(image):
            image[index]=values^int(key)
        f2=open(file_path, 'wb')
        f2.write(image)
        f2.close()

# text entry box
entered_key = Text(root, height=1, width=10)
entered_key.pack(side=TOP, pady=10)

# button
b1 = Button(root, text='Encrypt/Decrypt', command=encrypt_image)
b1.pack(side=TOP, pady=10)  # Center the button vertically and add vertical padding (10 pixels)

root.mainloop()