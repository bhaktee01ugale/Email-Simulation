import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image

# yashvi
class menu_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.pack()

# yashvi, snehal # same as display draft
class compose_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.pack()

# jessica
class display_sent_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.pack()

# bhaktee # same as sent window
class drafts_window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.pack()

#bhaktee
class sent_winodw(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.pack()

# jessica
class login_Window(ttk.Frame):
    def __int__(self, container):
        super().__init__(container)

        self.username = ttk.Label(self, text='Username')
        self.username.grid(row=0,column=0)

        self.input_username = ttk.Entry(self)
        self.input_username.grid(row=0, column=1)

        self.pack()

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
                return
            self.gif_label.configure(image=im2)
            self.after(50, animation, count)

        self.gif_label = ttk.Label(self)
        self.gif_label.pack()

        self.after(0, animation, 0)
        self.pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        icon = PhotoImage(file='Mail.png')

        self.title("Mail")

        self.iconphoto(False, icon)




if __name__ == '__main__':
    app = App()
    start = Start_Window(app)
    login = login_Window(app)
    app.mainloop()