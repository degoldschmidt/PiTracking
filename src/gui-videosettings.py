# import the necessary packages
import sys, math, cv2, os
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
        self.HALT = True
        self.mwidth = 480
        self.mheight = 270
        self.var = []
        self.conds = []
        self.root = self.mainWindow()
        self.cap = VideoCapture("PI").run()
        #self.getProperties()
        self.write = self.initWriter()

        """ Notebook structure """
        self.tabs = ttk.Notebook(self.root)
        self.f1 = Frame(self.tabs)   # first page, which would get widgets gridded into it
        self.f1 = self.tabInput(self.f1)
        self.f2 = Frame(self.tabs)   # second page
        self.f3 = Frame(self.tabs)   # third page
        self.tabs.add(self.f1, text='Input Settings')
        self.tabs.add(self.f2, text='Output Settings')
        self.tabs.add(self.f3, text='Recording')
        self.tabs.pack(fill=BOTH, expand=1)

    def mainWindow (self):
        root = Tk()
        root.lift()
        root.attributes("-topmost", 1)
        root.attributes("-topmost", 0)
        root.protocol("WM_DELETE_WINDOW", self.destr)
        root.configure(background='#000000')
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
        raw_image = self.cap.get()
        print(raw_image)
        if raw_image is not None:
            #cv2image = cv2.resize(raw_image,(self.mwidth, self.mheight), interpolation = cv2.INTER_CUBIC)
            cv2image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGBA)
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

    def getProperties(self):
        for ind in range(39):
            print(ind, ":", self.cap.getProperty(ind))

    def resetCapture(self):
        self.cap.stop()
        self.write.release()

    def setAspRatio(self, wval, hval):
        self.mheight = int(self.mwidth*(hval/wval))
        print("Set preview:", self.mwidth, self.mheight)
        self.imageFrame = LabelFrame(self.root, text="Live Preview", width=self.mwidth, height=self.mheight, labelanchor='n')
    def setBrightness(self, value):
        if not self.HALT:
            self.cap.setBrightness(float(value))
    def setContrast(self, value):
        if not self.HALT:
            self.cap.setContrast(float(value))
    def setExposure(self, value):
        if not self.HALT:
            self.cap.setExposure(float(value))
    def setFramerate(self, value):
        if not self.HALT:
            self.cap.setFramerate(float(value))
    def setGain(self, value):
        if not self.HALT:
            self.cap.setGain(float(value))
    def setHeight(self, value):
        if not self.HALT:
            self.cap.setHeight(float(value))
    def setHue(self, value):
        if not self.HALT:
            self.cap.setHue(float(value))
    def setResolution(self, value):
        self.resetCapture()
        #self.cap = VideoCapture("CV").run()
        """
        if self.dropVar.get() == "640x480@30Hz":
            self.cap.setWidth(640)
            self.cap.setHeight(480)
            self.setAspRatio(4,3)
        elif self.dropVar.get() == "800x600@30Hz":
            self.cap.setWidth(800)
            self.cap.setHeight(600)
            self.setAspRatio(4,3)
        elif self.dropVar.get() == "1024x768@30Hz":
            self.cap.setWidth(1024)
            self.cap.setHeight(768)
            self.setAspRatio(4,3)
        elif self.dropVar.get() == "1280x720@30Hz":
            self.cap.setWidth(1280)
            self.cap.setHeight(960)
            self.setAspRatio(16,9)
        elif self.dropVar.get() == "1280x960@30Hz":
            self.cap.setWidth(1280)
            self.cap.setHeight(960)
            self.setAspRatio(4,3)
        elif self.dropVar.get() == "1600x900@30Hz":
            self.cap.setWidth(1600)
            self.cap.setHeight(900)
            self.setAspRatio(16,9)
        elif self.dropVar.get() == "1920x1080@30Hz":
            self.cap.setWidth(1920)
            self.cap.setHeight(1080)
            self.setAspRatio(16,9)
        """
    def setSaturation(self, value):
        if not self.HALT:
            self.cap.setSaturation(float(value))
    def setWidth(self, value):
        if not self.HALT:
            self.cap.setWidth(float(value))

    def tabInput(self, parent):
        """ Live Preview """
        self.imageFrame = LabelFrame(parent, text="Live Preview", width=self.mwidth, height=self.mheight, labelanchor='n')
        self.imageFrame.grid(row=0, rowspan=6, column=0, columnspan=4, sticky=W+E+N+S)
        self.lmain = Label(self.imageFrame)
        self.lmain.grid(row=0, rowspan=6,  column=0)
        """ Video capture settings """
        bri = Scale(parent, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, command=self.setBrightness, label = 'Brightness')
        #bri.set(self.cap.getProperty(cv2.CAP_PROP_BRIGHTNESS))
        bri.grid(row=0, column=4)
        contr = Scale(parent, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, command=self.setContrast, label = 'Contrast')
        #contr.set(self.cap.getProperty(cv2.CAP_PROP_CONTRAST))
        contr.grid(row=1, column=4)
        expos = Scale(parent, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, label = 'Exposure', state=DISABLED)
        expos.grid(row=2, column=4)
        gain = Scale(parent, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, label = 'Gain', state=DISABLED)
        gain.grid(row=3, column=4)
        hue = Scale(parent, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, label = 'Hue', state=DISABLED)
        hue.grid(row=4, column=4)
        sat = Scale(parent, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, command=self.setSaturation, label = 'Saturation')
        #sat.set(self.cap.getProperty(cv2.CAP_PROP_SATURATION))
        sat.grid(row=5, column=4)
        """ Dropdown list """
        optionList = ["640x480@30Hz", "800x600@30Hz", "1024x768@30Hz", "1280x960@30Hz", "1600x1080@30Hz", "1920x1080@30Hz"]
        self.dropVar = StringVar()
        self.dropVar.set("1920x1080@30Hz") # default choice
        self.dropdown = OptionMenu(parent, self.dropVar, *optionList, command=self.setResolution)
        self.dropdown.grid(column=0, columnspan=2, row=6, sticky=W+E+N+S)
        return parent

    def initWriter(self):
        fps = 30.0
        size = (1920, 1080)
        destinationFile = 'out.avi'

        # These are the codecs I've tried so far
        #codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
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
