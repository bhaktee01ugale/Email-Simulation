import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image
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
            compose_window.tkraise(container)

        self.create = ttk.Button(self, text="Compose", command=lambda:create(self), cursor='hand2').place(anchor='center')

# yashvi, snehal # same as display draft
class compose_window(ttk.Frame):


    def __init__(self, container):
        super().__init__(container)
        container.geometry('500x520')

        def send(self):
            try:
                global smtp
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = self.subject.get(0, "end")
                msg.attach(MIMEText(self.body, 'plain'))

                smtp.sendmail(sender_email, receiver_email, msg)

                smtp.quit()

                print("Email sent Successfully!")
                messagebox.showinfo("Status", "Email sent Successfully!")
            except Exception as ex:
                messagebox.showerror("Error", "Something went wrong!")
                print('Something went wrong!', ex)

        self.t_l = ttk.Label(self, text="To").grid(row=0, column=0)
        self.to = ttk.Entry(self).grid(row=0, column=1)
        self.s_l = ttk.Label(self, text="Subject").grid(row=1, column=0)
        self.subject = ttk.Entry(self).grid(row=1, column=1)

        self.body = tk.Text(self, width=50).grid(row=2, columnspan=2)
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
                messagebox.showerror("Error", "Login unsuccessful!")
                print('Something went wrong!', ex)
        self.input_username = ttk.Entry(self, width=40)
        self.input_username.grid(row=1, column=1)
        self.input_username.insert(0, "Username")
        self.input_username.bind("<FocusIn>", self.temp_text_user)
        self.input_username.bind("<FocusOut>", self.on_focusout_user)
        self.input_username.configure(foreground='grey')
        self.input_username.get()

        self.input_password = ttk.Entry(self, width=40)
        self.input_password.grid(row=2, column=1)
        self.input_password.insert(0, "Password")
        self.input_password.bind("<FocusIn>", self.temp_text_pass)
        self.input_password.bind("<FocusOut>", self.on_focusout_pass)
        self.input_password.configure(foreground='grey')
        self.input_password.get()
        self.Login = ttk.Button(self, text='LOGIN', command=lambda : set(self), cursor='hand2')
        self.Login.grid(row=4, column=1)

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
                login_Window(container).grid(row=0, column=0)
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
        app.mainloop()
    except Exception as ex:
        messagebox.showerror("Error", "No internet connectivity!")
