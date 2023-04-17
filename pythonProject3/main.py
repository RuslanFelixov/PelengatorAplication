from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from logic import *

class App:
    def __init__(self):
        self.root = Tk()

        # создаем рабочую область
        self.frame = Frame(self.root)
        self.frame.grid()

        # тип цели
        self.labelAim = Label(self.root, text="Тип цели", font=("Arial Bold", 12))
        self.labelAim.grid()

        self.listAim = Combobox(self.root, state="readonly", values=('Буй', 'НПА', 'АПЛ'), font=("Arial Bold", 12))
        self.listAim.grid()

        # пеленг
        self.labelPeleng = Label(self.root, text="Пеленг угла", font=("Arial Bold", 12))
        self.labelPeleng.grid()

        self.scalePeleng = Scale(self.root, from_=-90, to=90, orient=HORIZONTAL, length=280, width=20)
        self.scalePeleng.grid()

        # дистанция
        self.labelDist = Label(self.root, text="Дистанция", font=("Arial Bold", 12))
        self.labelDist.grid()

        self.scaleDist = Scale(self.root, from_=50, to=1000, orient=HORIZONTAL, length=280, width=20)
        self.scaleDist.grid()

        self.result = Label(self.root, text='', font=("Arial Bold", 12))
        self.result.grid()

        # вставляем кнопку
        self.but = Button(self.frame, text="Расчет", command=self.my_event_handler)
        self.but.grid()

        # Добавим изображение #блок
        self.canvas = Canvas(self.root, height=620, width=800)
        self.root.mainloop()

    def my_event_handler(self):
        type = self.listAim.get()
        Long = self.scaleDist.get()
        alfa = self.scalePeleng.get()

        coefObj = 1
        if type == 'Буй':
            coefObj = 1
        elif type == 'НПА':
            coefObj = 4
        else:
            coefObj = 6

        dataObj = collBack(alfa, Long, coefObj)
        peleng, distance, name = dataObj.getPeleng(), dataObj.getDistance(), dataObj.getName()

        сonclusion = 'Пеленг: {0} гр, дистанция: {1} м, тип цели: {2}'.format(peleng, distance, name)
        self.result.config(text=сonclusion)

        self.image = Image.open("signal.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.image1 = Image.open("filter.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.image2 = Image.open("grid.png")
        self.photo2 = ImageTk.PhotoImage(self.image2)

        self.image3 = Image.open("response.png")
        self.photo3 = ImageTk.PhotoImage(self.image3)

        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.c_image1 = self.canvas.create_image(400, 0, anchor='nw', image=self.photo1)
        self.c_image2 = self.canvas.create_image(0, 310, anchor='nw', image=self.photo2)
        self.c_image3 = self.canvas.create_image(400, 310, anchor='nw', image=self.photo3)

        self.canvas.grid()

app= App()




