from tkinter import *
import cv2
from PIL import Image, ImageTk
import time
from tkinter import filedialog


class App:
    def __init__(self, video_source=0):
        self.appName = "Camera"
        self.window = Tk()
        self.window.title(self.appName)
        self.window.resizable(0, 0)
        # self.window.wm_iconbitmap("cam.ico")
        self.window['bg'] = 'black'
        self.video_source = video_source

        self.vid = MyVideoCapture(self.video_source)
        # self.label = Label(self.window, text=self.appName, font=15, bg='blue', fg='white').pack(side=TOP, fill=BOTH)
        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height, bg='red')
        self.canvas.pack()

        self.btn_snapshot = Button(self.window, text="Captura", width=5, command=self.snapshot)
        self.btn_snapshot.pack(side=LEFT, padx=10)

        self.btn_flip = Button(self.window, text="Virar imagem", width=7, command=self.flip_img)
        self.btn_flip.pack(side=LEFT, padx=10)

        self.btn_overlay = Button(self.window, text="Sobrepor", width=7, command=self.overlay)
        self.btn_overlay.pack(side=LEFT, padx=10)

        self.update()
        self.window.mainloop()

    def flip_img(self):
        self.vid.flipped = not self.vid.flipped

    def overlay(self):
        file = filedialog.askopenfile(
            mode='rb', defaultextension='.png', title="Choose Overlay Image", filetypes=[("PNG Files", '*.png')])
        if file:
            self.overlay_img = ImageTk.PhotoImage(file=file)
            self.canvas.tag_raise(self.overlay_img)
            self.canvas.create_image(0, 0, image=self.overlay_img, anchor=NW)

    def snapshot(self):
        check, frame = self.vid.getFrame()
        if check:
            image = "./img/desconhecido.jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            msg = Label(self.window, text='imagem salva!' + image, bg='black', fg='green').place(x=430, y=510)

        else:
                messagebox.showerror("paint says", "não foi possível salvar a imagem,\n algo deu errado")

    def update(self):
        isTrue, frame = self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.tag_lower(self.photo)
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(15, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open this camera \n select another video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.flipped = True

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue and self.flipped:
                frame = cv2.flip(frame, 1)
            if isTrue:
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
        else:
            return (isTrue, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


if __name__ == "__main__":
    App()