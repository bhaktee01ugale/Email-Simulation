import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image
from tkinter.ttk import Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox


# yashvi
class menu_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        def create(self):
            compose_window(container).grid(row=0,column=0)
            self.destroy()


        self.l = ttk.Label(self, width=30).grid(row=0, column=0)
        self.create = ttk.Button(self, text='Compose', command=lambda: create(self), cursor='hand2').grid(row=1, column=1)
        self.rowconfigure(0, weight=3)
        self.columnconfigure(0, weight=3)

# yashvi, snehal # same as display draft
class compose_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        container.geometry('500x520')

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
                print(body)
                global smtp
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body))

                smtp.send_message(msg)

                smtp.quit()

                print("Email sent Successfully!")
                messagebox.showinfo("Status", "Email sent Successfully!")
            except Exception as ex:
                messagebox.showerror("Error", "Something went wrong!")
                print('Something went wrong!', ex)

        self.t_l = ttk.Label(self, text="To").grid(row=0, column=0)
        self.to = ttk.Entry(self, width=10)
        self.to.grid(row=0, column=1)
        self.to.get()
        self.s_l = ttk.Label(self, text="Subject").grid(row=1, column=0)
        self.sub = ttk.Entry(self)
        self.sub.grid(row=1, column=1)
        self.sub.get()

        self.body = tk.Text(self, width=50)
        self.body.grid(row=2, columnspan=2)
        self.body.get("1.0", 'end-1c')

        self.send_button = ttk.Button(self, text="Send", cursor='hand2',command=lambda: send(self)).grid(row=3, column=1)



# jessica
class display_sent_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)



# bhaktee # same as sent window
class drafts_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)



#bhaktee
class sent_winodw(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)



# jessica
class login_Window(ttk.Frame):
    def temp_text_user(self, e):
        self.input_username.delete(0, "end")
        self.input_username.configure(foreground='black')

    def temp_text_pass(self, e):
        self.input_password.delete(0, "end")
        self.input_password.configure(foreground='black')
        self.input_password.configure(show="*")

    def on_focusout_pass(self, e):
        if self.input_password.get() == '':
            #self.input_password.delete(0, "end")
            self.input_password.insert(0, 'Password')
            self.input_password.configure(foreground='grey')

    def on_focusout_user(self, e):
        if self.input_username.get() == '':
            #self.input_password.delete(0, "end")
            self.input_username.insert(0, 'Username')
            self.input_username.configure(foreground='grey')

    def __init__(self, container):
        super().__init__(container)

        self.sender = ''
        self.password = ''

        def set(self):
            global sender_email
            sender_email = sender_email + self.input_username.get()
            global password
            password = password + self.input_password.get()
            try:
                global smtp
                smtp.login(sender_email, password)
                print("Logged in Successfully!")
                messagebox.showinfo("Status", "Logged In Successfully!")
                self.input_password.destroy()
                self.input_username.destroy()
                menu_window(container).grid(row=0, column=0)
                self.destroy()
            except Exception as ex:
                messagebox.showerror("Error", "Wrong Credentials!")
                print('Something went wrong!', ex)

        container.geometry('565x378')
        self.input_username = ttk.Entry(self, width=35)
        self.input_username.grid(row=1, column=1)
        self.input_username.insert(0, "Username")
        self.input_username.bind("<FocusIn>", self.temp_text_user)
        self.input_username.bind("<FocusOut>", self.on_focusout_user)
        self.input_username.configure(foreground='grey', font='Helvetica 15')
        self.input_username.get()

        self.input_password = ttk.Entry(self, width=35)
        self.input_password.grid(row=2, column=1)
        self.input_password.insert(0, "Password")
        self.input_password.bind("<FocusIn>", self.temp_text_pass)
        self.input_password.bind("<FocusOut>", self.on_focusout_pass)
        self.input_password.configure(foreground='grey', font='Helvetica 15')
        self.input_password.get()

        style = Style()

        style.configure('W.TButton', font=
        ('Helvetica', 15, 'bold'),
                        foreground='black')
        self.Login = ttk.Button(self, text='LOGIN', command=lambda : set(self), cursor='hand2', style='W.TButton').grid(row=4, column=1)
        #self.Login['Font'] = self.myFont


        self.t = ttk.Label(self, width=10).grid(row=0, columnspan=3)
        self.t_c = ttk.Label(self, width=10).grid(row=1, column=0)
        self.b_r = ttk.Label(self, width=10).grid(row=3, columnspan=3)
        self.columnconfigure(index=0, weight=2)

        #self.grid(row=0, column=0)



# bhaktee
class Start_Window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        file = 'mail-download.gif'
        info = Image.open(file)
        frames = info.n_frames

        im = [PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]

        count = 0

        def animation(count):
            im2 = im[count]
            count += 1
            if count == frames:
                self.gif_label.destroy()
                login_Window(container).place(anchor=tk.NW)
                self.destroy()
                return
            self.gif_label.configure(image=im2)
            self.after(50, animation, count)

        self.gif_label = ttk.Label(self)
        self.gif_label.pack()

        self.after(0, animation, 0)
        #self.grid(row=0, column=0)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x378')

        icon = PhotoImage(file='Mail.png')

        self.title("Mail")

        self.iconphoto(False, icon)

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
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        print("Session Started!")

        smtp.starttls()
        app = App()
        sender_email = ''
        password = ''
        receiver_email = ''
        body = ""
        subject=''
        app.mainloop()
    except Exception as ex:
        messagebox.showerror("Error", "No internet connectivity!")
