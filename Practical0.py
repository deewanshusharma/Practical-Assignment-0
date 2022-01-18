import tkinter as tk
Mywin = tk.Tk()

#Function to convert plain text to cipher text
def encipher():
    #Clearing the output textbox's (textbox2 in this case) data.
    textbox2.delete(0,'end')
    plain=textbox1.get()
    #res string will store the converted text as a string and at the end of this function, it'll be inserted in the respective textbox
    res=""
    for i in range (len(plain)):
        char=plain[i]
        #Lower case and the upper case letters will be treated seperatedly
        if(char.isupper()):
            res+=chr(ord('Z') - ord(char) + ord('A'))
        elif(char.islower()):
            res+=chr(ord('z') - ord(char) + ord('a'))
        else:
            res+=char
    textbox2.insert(0,res)

#Function to convert cipher text to plain text
def decipher():
    textbox1.delete(0,'end')
    plain=textbox2.get()
    res=""
    for i in range (len(plain)):
        char=plain[i]
        if(char.isupper()):
            res+=chr(ord('Z') - ord(char) + ord('A'))
        elif(char.islower()):
            res+=chr(ord('z') - ord(char) + ord('a'))
        else:
            res+=char
    textbox1.insert(0,res)
    

#Plain text portion containing label, textbox and a button to encipher
label1 = tk.Label(Mywin, text="Plain Text")
label1.grid(row=1,column=1)

textbox1 = tk.Entry(Mywin, text="Plain Text")
textbox1.grid(row=2,column=1,padx=10,pady=10,ipadx=80,ipady=80)

button1 = tk.Button(Mywin, text="Encipher",bg='blue',padx=10,pady=10, command=encipher)
button1.grid(row=3,column=1)

#Cipher text portion containing label, textbox and a button to decipher
label2 = tk.Label(Mywin, text="Cipher Text")
label2.grid(row=1,column=8)

textbox2 = tk.Entry(Mywin, text="Cipher Text")
textbox2.grid(row=2,column=8,padx=10,pady=10,ipadx=80,ipady=80)

button2 = tk.Button(Mywin, text="Decipher",bg='blue',padx=10,pady=10, command=decipher)
button2.grid(row=3,column=8)

Mywin.title("Practical 0")
Mywin.mainloop()
