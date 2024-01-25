from tkinter import *
import base64
import os
from tkinter import messagebox

def decrypt():
    passw=code.get()
    #gets the passphrase entered

    if passw=="9900": #the passcode is hardcoded for now, here
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#ed3833")

        message= text1.get(1.0, END) #gets the texts from the 1st entrybox
        decd_msg=message.encode("ascii") #encodes that message to ASCII
        bs64_b=base64.b64decode(decd_msg) #using B64 encoding to encode the ASCII message
        encr=bs64_b.decode("ascii") #decoding the message to characters from ASCII

        #the label on the new screen
        Label(screen2, text="Decrypted Message", font="times", fg="white", bg="#ed3833").place(x=10, y=10)

        #the textbox on the new screen
        text2=Text(screen2, font="Robote 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        #inserting the encrypted text
        text2.insert(END, encr)

    elif passw=="":
        messagebox.showerror("Encryption", "No input in the key section!")

    else:
        messagebox.showerror("Encryption", "You entered a wrong key!")

#defining the encrypt function
def encrypt():
    passw=code.get()
    #gets the passphrase entered

    if passw=="9900": #the passcode is hardcoded for now, here
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message= text1.get(1.0, END) #gets the texts from the 1st entrybox
        encd_msg=message.encode("ascii") #encodes that message to ASCII
        bs64_b=base64.b64encode(encd_msg) #using B64 encoding to encode the ASCII message
        encr=bs64_b.decode("ascii") #decoding the message to characters from ASCII

        #the label on the new screen
        Label(screen1, text="Encrypted Message", font="times", fg="white", bg="#ed3833").place(x=10, y=10)

        #the textbox on the new screen
        text2=Text(screen1, font="Robote 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        #inserting the encrypted text
        text2.insert(END, encr)

    elif passw=="":
        messagebox.showerror("Encryption", "No input in the key section!")

    else:
        messagebox.showerror("Encryption", "You entered a wrong key!")





def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("800x550")

    image_i=PhotoImage(file="keys.png") #adds the icon, apparently not working
    screen.iconphoto(False, image_i)

    screen.title("Message Encypter/Decryptor") #adds the title of the GUI

    #defining the reset function
    def reset():
        code.set("")
        text1.delete(1.0, END)

    #the first label
    Label(text="Enter text for Encyrption/Decryption: ", fg="black", font=("Times New Roman", 20)).place(x=10, y=10)
    
    #the first entry box to type the message
    text1=Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=750, height=200)

    #the second label
    Label(text="Enter the key for encryption and decryption:", fg="black", font=("Times New Roman", 20)).place(x=10, y=270)
    
    #the second entry box to type in the passphrase
    code=StringVar()
    Entry(textvariable=code, width=50, bd=0, font=("Robote", 18), show="*").place(x=10, y=310) #the second entry box which shows * to hide and takes the input in the form of a string

    #encrypt button
    Button(text="ENCRYPT", height="4", width="45", bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=350)

    #decrypt button
    Button(text="DECRYPT", height="4", width="45", bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=400, y=350)

    #reset button
    Button(text="RESET", height="4", width="94", bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=435)

    screen.mainloop()


main_screen()