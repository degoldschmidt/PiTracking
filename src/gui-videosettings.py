# import the necessary packages
import sys
import math
import cv2
import numpy as np
""" Compability check for Python """
if sys.version_info >= (3,0):
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import filedialog
    from PIL import Image, ImageTk
else:
    from Tkinter import *
    from PIL import Image, ImageTk
    import ttk as ttk
    import tkMessageBox as messagebox
    import tkFileDialog as filedialog
# Camera capture class
from vidcapture import VideoCapture
from cvcapture import CVVideoCapture

class App():
    def __init__ (self):
        self.var = []
        self.conds = []
        self.root = self.mainWindow()
        self.cap = VideoCapture("CV").run()
        self.mwidth = 480
        self.mheight = 270
        self.imageFrame = LabelFrame(self.root, text="Live Preview", width=self.mwidth, height=self.mheight, labelanchor='n')
        self.imageFrame.grid(row=0, column=0, padx=10, pady=2)
        self.lmain = Label(self.imageFrame)
        self.lmain.grid(row=0, column=0)
        self.write = self.initWriter()
        w = Scale(self.root, from_=-1, to=1, orient=HORIZONTAL, resolution=0.01, command=self.setBrightness)
        w.grid(row=1, column=0)

    def mainWindow (self):
        root = Tk()
        root.lift()
        root.attributes("-topmost", 1)
        root.attributes("-topmost", 0)
        root.protocol("WM_DELETE_WINDOW", self.destr)
        root.configure(background='#ffffff')
        root.title("Raspberry Pi Camera V2 Settings GUI")
        root.resizable(width=True, height=True)
        #root.geometry("650x900")


        # create a menu
        root.config(menu=self.getMenu(root))

        #root = self.getTop(root)
        #root = self.getCenter(root)
        #root = self.getBottom(root)

        return root

    def destr(self):
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.cap.stop()
            self.write.release()
            self.root.destroy()

    """ TODO """
    def displayFrame(self):
        #Graphics window
        cv2image = cv2.flip(self.cap.get(), 1)
        cv2image = cv2.resize(cv2image,(self.mwidth, self.mheight), interpolation = cv2.INTER_CUBIC)
        cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
        cv2image = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=cv2image)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.displayFrame)

    def getMenu(self, root):
        rootmenu = Menu(root)

        ### File entry
        filemenu = Menu(rootmenu)
        rootmenu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open...")
        filemenu.add_command(label="Save...")
        filemenu.add_separator()
        filemenu.add_command(label="Import...")
        filemenu.add_command(label="Export...")
        filemenu.add_separator()
        filemenu.add_command(label="Exit")

        ### View entry
        viewmenu = Menu(rootmenu)
        rootmenu.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="View experiment")
        viewmenu.add_command(label="View history")

        ### Help entry
        helpmenu = Menu(rootmenu)
        rootmenu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...")

        return rootmenu

    def setBrightness(self, value):
        self.cap.setBrightness(float(value))

    def initWriter(self):
        fps = 20.0
        size = (1280, 720)
        destinationFile = 'out.mp4'

        # These are the codecs I've tried so far
        codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        video  = cv2.VideoWriter(destinationFile, codec, fps, size);
        if video is None:
            print('Warning: unable to create video writer')
        else:
            print('initialized writer')
        return video

    def capture(self):
        try:
            frame = self.cap.get()
            frame = cv2.flip(frame,0)
            self.write.write(frame)
        except:
            print("Unexpected error: ", sys.exec_info()[0])

def main():
    app = App()
    app.displayFrame()
    #app.capture()
    app.root.mainloop()

if __name__ == '__main__':
    main()
