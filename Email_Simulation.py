import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image
from tkinter.ttk import Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox



class menu_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)  # to invoke parent constructor

        #container.geometry('560x378')

        def create(self):
            compose_window(container).grid(row=0,column=0)
            compose_window.tkraise(container)

        style = Style()

        style.configure('W.TButton', font=
        ('Helvetica', 15, 'bold'),
                        foreground='black')

        self.l = ttk.Label(self,width=10)
        self.l.grid(row=0, column=0)
        self.l.configure(foreground='black', font='Helvetica 20')
        self.create = ttk.Button(self, text='Compose', command=lambda: create(self), cursor='hand2', style='W.TButton').grid(row=1, column=1)
        self.rowconfigure(0, weight=3)
        self.columnconfigure(0, weight=2)


class compose_window(ttk.Frame):
    def temp_text_to(self, e):
        self.to.delete(0, "end")
        self.to.configure(foreground='black')

    def temp_text_sub(self, e):
        self.sub.delete(0, "end")
        self.sub.configure(foreground='black')

    def on_focusout_to(self, e):
        if self.to.get() == '':
            #self.to.delete(0, "end")
            self.to.insert(0, 'Recipient')
            self.to.configure(foreground='grey')

    def on_focusout_sub(self, e):
        if self.sub.get() == '':
            #self.input_password.delete(0, "end")
            self.sub.insert(0, 'Subject')
            self.sub.configure(foreground='grey')

    def __init__(self, container):
        super().__init__(container)  # to invoke parent constructor
        container.geometry('555x555')

        def send(self):
            try:
                global receiver_email
                receiver_email = receiver_email + self.to.get()
                print("Recipient:",receiver_email)
                global subject
                subject = subject + self.sub.get()
                print("Subject line:",subject)
                global body
                body = body + self.body.get("1.0", 'end-1c')
                print("Body of email:",body)
                global smtp
                # To create message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body))


                smtp.send_message(msg)  # To send email

                smtp.quit() # to disconnect from the server

                print("Email sent Successfully!")
                messagebox.showinfo("Status", "Email sent Successfully!")
                container.destroy()
            except Exception as ex:
                messagebox.showerror("Error", "Something went wrong!")
                print('Something went wrong!', ex)

        # Recipient field
        self.to = ttk.Entry(self, width=50)
        self.to.grid(row=0, column=0)
        self.to.insert(0, "Recipient")
        self.to.bind("<FocusIn>", self.temp_text_to)
        self.to.bind("<FocusOut>", self.on_focusout_to)
        self.to.configure(foreground='grey', font='Helvetica 15')
        self.to.get()

        # Subject line

        #self.s_l = ttk.Label(self, text="Subject").grid(row=1, column=0)
        self.sub = ttk.Entry(self, width=50)
        self.sub.grid(row=1, column=0)
        self.sub.insert(0, "Subject")
        self.sub.bind("<FocusIn>", self.temp_text_sub)
        self.sub.bind("<FocusOut>", self.on_focusout_sub)
        self.sub.configure(foreground='grey', font='Helvetica 15')
        self.sub.get()

        # Body for email
        self.body = tk.Text(self, width=50)
        self.body.grid(row=2, column=0)
        self.body.get("1.0", 'end-1c')

        self.l = ttk.Label(self, width=50).grid(row=3, column=0)

        style = Style()

        style.configure('W.TButton', font=
        ('Helvetica', 15, 'bold'),
                        foreground='black')

        # send button
        self.send_button = ttk.Button(self, text="Send", cursor='hand2',command=lambda: send(self), style='W.TButton').grid(row=4, column=0)




class login_Window(ttk.Frame):

    # to delete default text in username field
    def temp_text_user(self, e):
        self.input_username.delete(0, "end")
        self.input_username.configure(foreground='black')

    # to delete default text in password field
    def temp_text_pass(self, e):
        self.input_password.delete(0, "end")
        self.input_password.configure(foreground='black')
        self.input_password.configure(show="*")

    # to enter default text in password field
    def on_focusout_pass(self, e):
        if self.input_password.get() == '':
            #self.input_password.delete(0, "end")
            self.input_password.insert(0, 'Password')
            self.input_password.configure(foreground='grey')

    # to enter default text in username field
    def on_focusout_user(self, e):
        if self.input_username.get() == '':
            #self.input_password.delete(0, "end")
            self.input_username.insert(0, 'Username')
            self.input_username.configure(foreground='grey')

    def __init__(self, container):
        super().__init__(container) # to invoke parent constructor

        def set(self):
            global sender_email
            sender_email = sender_email + self.input_username.get()
            global password
            password = password + self.input_password.get()
            try:
                global smtp

                smtp.login(sender_email, password)  # to login with given credentials

                print("Logged in Successfully!")
                messagebox.showinfo("Status", "Logged In Successfully!")
                self.input_password.destroy()
                self.input_username.destroy()
                menu_window(container).grid(row=0, column=0)  # to create menu window
                self.destroy()
            except Exception as ex:
                messagebox.showerror("Error", "Wrong Credentials!\nRestart program!")
                print('Something went wrong!', ex)

        container.geometry('565x378')

        self.ph = ttk.Label(self, text="Welcome to Mail")
        self.ph.grid(row=1, column=1)
        self.ph.configure(foreground='black', font='Helvetica 20')

        # username field
        self.input_username = ttk.Entry(self, width=35)
        self.input_username.grid(row=3, column=1)
        self.input_username.insert(0, "Username")
        self.input_username.bind("<FocusIn>", self.temp_text_user)
        self.input_username.bind("<FocusOut>", self.on_focusout_user)
        self.input_username.configure(foreground='grey', font='Helvetica 15')
        self.input_username.get()

        # password field
        self.input_password = ttk.Entry(self, width=35)
        self.input_password.grid(row=4, column=1)
        self.input_password.insert(0, "Password")
        self.input_password.bind("<FocusIn>", self.temp_text_pass)
        self.input_password.bind("<FocusOut>", self.on_focusout_pass)
        self.input_password.configure(foreground='grey', font='Helvetica 15')
        self.input_password.get()

        # to create style object
        style = Style()

        style.configure('W.TButton', font=
        ('Helvetica', 15, 'bold'),
                        foreground='black')

        # login button
        self.Login = ttk.Button(self, text='Login', command=lambda : set(self), cursor='hand2', style='W.TButton').grid(row=6, column=1)
        #self.Login['Font'] = self.myFont


        self.t = ttk.Label(self, width=10).grid(row=0, columnspan=3)
        self.t_c = ttk.Label(self, width=10).grid(row=1, column=0)
        self.b_r = ttk.Label(self, width=10).grid(row=5, columnspan=3)
        self.columnconfigure(index=0, weight=2)
        self.w = ttk.Label(self, width=10).grid(row=2, column=0)

        #self.grid(row=0, column=0)




class Start_Window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)  # to invoke parent constructor

        file = 'mail-download.gif'
        info = Image.open(file)  # to open the gif
        frames = info.n_frames # to find number of photos of gif

        im = [PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]  # list to store photos of gif

        count = 0  # to save index of images

        # to run the gif
        def animation(count):

            im2 = im[count] # to access the image of index count

            count += 1

            # if displaying of all photos is complete
            if count == frames:
                self.gif_label.destroy()  # destroy the label which displays gif

                login_Window(container).place(anchor=tk.NW)   # creating login_window

                self.destroy()  # to destroy the current window
                return

            self.gif_label.configure(image=im2)  # to display image
            self.after(50, animation, count) # to run

        self.gif_label = ttk.Label(self)  # label to display gif
        self.gif_label.pack()

        self.after(0, animation, 0)
        #self.grid(row=0, column=0)


class App(tk.Tk):
    def __init__(self):
        super().__init__() # to invoke parent constructor

        self.geometry('500x378') #to set the size of winodow

        icon = PhotoImage(file='Mail.png') # to open icon image

        self.title("Mail")  # to set title

        self.iconphoto(False, icon) # to set icon of tkinter window

        self.resizable(False, False)  # to disable resize button

        '''self.frames = {}
        for F in (Start_Window, login_Window, compose_window):
            frame = F(self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0)
            frame.grid_forget()'''
        Start_Window(self).grid(row=0, column=0)
        #self.show_frame(Start_Window)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




if __name__ == "__main__" :

    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)  # to set connection with server
        print("Session Started!")

        smtp.starttls()  # to securely connect with server
        app = App()
        sender_email = ''   # email address of the sender
        password = ''   # password of the sender's account
        receiver_email = '' # email address of the receiver
        body = ""   # body of email
        subject=''  # subject of email
        app.mainloop()
    except Exception as ex:
        messagebox.showerror("Error", "No internet connectivity!")
