from tkinter import *
from tkinter import font


class TiledButton(Frame):
    def __init__(self, parent, h, w, text=None, image=None, command=None, color="black", font=None, bg=None):
        super(TiledButton, self).__init__(parent)
        self.font = font
        self.text = text
        self.imagepath = image
        self.color = color
        self.canv = Canvas(self, width=w, height=h, bg=bg)
        self.command = command
        self.h, self.w = h, w
        self.canv.pack()
        if self.imagepath is not None:
            self.load_image()
        if text is not None:
            self.canv.create_text(self.w // 2, self.h // 2, text=self.text, fill=self.color, font=font)
        self.canv.create_rectangle(0, 0, self.w, self.h, fill="", outline="", tags="button")
        self.canv.tag_bind("button", "<Button-1>", self.clicked)

    def load_image(self):
        print("load image called")
        self.img = PhotoImage(file=self.imagepath)
        self.canv.create_image((self.w // 2, self.h // 2), image=self.img)

    def clicked(self, event):
        # event.widget['bg']='blue'
        if self.command is None:
            return
        print("Clicked of widget called")
        self.command()


# driver code
# root = Tk()
#
#
# def hello():
#     print("I said hello!!")
#
#
# TiledButton(root, command=hello, text="Button", h=100, w=100,
#             image="C:\\Users\\Balarubinan\\Desktop\\UNO_cards\\UNOMR.png").pack()
# root.mainloop()
