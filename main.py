from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        #Background Image

        self.bg=ImageTk.PhotoImage(file="D:/Python Code/Login Page/images/background.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=48, y=50, width=500, height=450) 

        #Title and Subtitle
        title = Label(Frame_login, text="Login", font=("Impact", 35,"bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle = Label(Frame_login, text="Member Login", font=("Calibri", 15,"bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)

        #Username 
        lbl_username = Label(Frame_login, text="Username", font=("Calibri", 13), fg="grey", bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login, font=("Calibri", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width= 320, height= 35)

        #Password
        lbl_password = Label(Frame_login, text="Password", font=("Calibri", 13), fg="grey", bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Calibri", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width= 320, height= 35)

        #Button
        forget= Button(Frame_login, text="Forgot Password?", border= 0, font=("Calibri", 15,"bold"), fg="#6162FF", bg="white").place(x=90, y=280)
        submit= Button(Frame_login, text="Login", border= 0, command=self.check_function, font=("Calibri", 15,"bold"), fg="White", bg="#6162FF").place(x=90, y=320, width=180, height=40)

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required!", parent=self.root)

        elif self.username.get()!= "Admin" or self.password.get()!= "Admin@1234":
            messagebox.showerror("Error","All fields are required!", parent=self.root)

        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")



root = Tk()
obj = Login(root)
root.mainloop()