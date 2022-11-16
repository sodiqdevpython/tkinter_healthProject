from pathlib import Path

from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


global name
name = 'github.com/sodiqoydinov'


def form():
    if entry_1.get() and entry_2.get() and pol.get():
        global fio, yosh, jins
        fio = entry_1.get()
        yosh = entry_2.get()
        jins = pol.get()
        window1.destroy()
    else:
        messagebox.showerror('Ошибка!', 'Все формы обязательны')

#                                       Next 1


def next1():
    if (entry_1.get() and entry_2.get()) and smoke.get():
        global sad, dad, smokeResult
        sad = entry_1.get()
        dad = entry_2.get()
        smokeResult = smoke.get()
        global numIntVar
        numIntVar = 0
        global lst
        lst = [var1, var2, var3, var4, var5, var6,
               var7, var8, var9, var10, var11, var12]
        for i in lst:
            numIntVar += i.get()
        window.destroy()
    else:
        messagebox.showerror(
            'Ошибка', 'Употребление алкоголя, САД мм.рт.ст и ДАД мм.рт.ст необходимый')
#


def next2():
    if entry_1.get() and entry_2.get() and entry_3.get() and entry_4.get():
        global f01, f02, f03, f04, f1, f2, f3, imt
        f01 = entry_1.get()
        f02 = entry_2.get()
        f03 = entry_3.get()
        f04 = entry_4.get()
        f1 = round(float(f01)/float(f02), 2)
        f2 = round((float(f04)/(float(f03)**2)), 4)
        f3 = f2*10000
        if f3 >= 19 and f3 <= 24.9:
            imt = 'Норма'
        elif f3 >= 25 and f3 <= 29.9:
            imt = 'Предожирение'
        elif f3 >= 30 and f3 <= 34.9:
            imt = 'Первая степень ожирения'
        elif f3 >= 35 and f3 <= 39.9:
            imt = 'Вторая степень'
        elif f3 >= 40 and f3 <= 44.9:
            imt = 'Третья степень'
        elif f3 >= 45:
            imt = 'Четвертая степень'
        else:
            imt = 'Не соответствует требованию'
        window2.destroy()
    else:
        messagebox.showerror('Ошибка', 'Все формы обязательны')

#                                       Start of main function


def result():
    if jins == 'Мужской':
        try:
            entr1 = float(entry_1.get())
        except:
            entr1 = 1
        if numIntVar >= 4:
            result = ('Очень высокий риск')
        elif (lst[8].get()) == 1 and entr1 >= 6.9 and numIntVar < 4:
            result = ('Высокий риск')
        elif numIntVar == 0 and smokeResult == 2:
            result = ('Низкий риск')
        elif numIntVar == 2:
            result = ('Умеренный риск')
        else:
            result = ('Высокий риск')
    else:
        try:
            entr1 = float(entry_1.get())
        except:
            entr1 = 1
        if numIntVar >= 4:
            result = ('Очень высокий риск')
        elif (lst[8].get()) == 1 and entr1 >= 5.1 and numIntVar < 4:
            result = ('Высокий риск')
        elif numIntVar == 0 and smokeResult == 2:
            result = ('Низкий риск')
        elif numIntVar == 2:
            result = ('Умеренный риск')
        else:
            result = ('Высокий риск')
    if entry_6 and entry_4:
        ka = float(entry_4.get())-float(entry_6.get())
    else:
        messagebox.showerror(
            'Ошибка', 'ЛПВП  и  Общий холестерин обязательны')
    messagebox.showinfo(
        'Результат', f"\t{result}\t\nСоотношение окружность: {f1}\n ИМТ: {f2}\n Наличие и степень ожирения по ИМТ: {imt}\n Коэффицент атерогенности: {ka}")


    #                                       End of main function
window1 = Tk()
screen_width = window1.winfo_screenwidth()
screen_height = window1.winfo_screenheight()
x = (screen_width/2) - (751/2)
y = (screen_height/2) - (450/2)
window1.geometry(f'{751}x{450}+{int(x)}+{int(y)}')
window1.geometry("751x450")
window1.configure(bg="#FFFFFF")
window1.title(name)

canvas = Canvas(
    window1,
    bg="#FFFFFF",
    height=450,
    width=751,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("img1.png"))
image_1 = canvas.create_image(
    375.0,
    225.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("e1.png"))
entry_bg_1 = canvas.create_image(
    467.0000000000001,
    135.00000000000006,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=335.0000000000001,
    y=115.00000000000006,
    width=264.0,
    height=38.0
)

canvas.create_text(
    327.0000000000001,
    63.00000000000006,
    anchor="nw",
    text="Ф.И.О.",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    327.0000000000001,
    178.00000000000006,
    anchor="nw",
    text="Возраст",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    327.0000000000001,
    283.00000000000006,
    anchor="nw",
    text="Пол",
    fill="#000000",
    font=("Inter", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("e2.png"))
entry_bg_2 = canvas.create_image(
    395.0000000000001,
    244.00000000000006,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=335.0000000000001,
    y=228.00000000000006,
    width=120.0,
    height=30.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("btn1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=form,
    relief="flat"
)
button_1.place(
    x=530.0000000000001,
    y=398.00000000000006,
    width=162.0,
    height=32.0
)

canvas.create_text(
    125.00000000000011,
    16.000000000000057,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter", 24 * -1)
)

pol = IntVar()
Radiobutton(window1, variable=pol,
            value=1, font=('Helvetica', 11)).place(x=330, y=330)
canvas.create_text(
    365,
    335,
    anchor="nw",
    text="Мужской",
    fill="#000000",
    font=("Inter", 16 * -1)
)

Radiobutton(window1, variable=pol,
            value=2, font=('Helvetica', 11)).place(x=440, y=330)
canvas.create_text(
    475,
    335,
    anchor="nw",
    text="Женский",
    fill="#000000",
    font=("Inter", 16 * -1)
)

window1.resizable(False, False)
window1.mainloop()


#                            Test2


window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (1300/2)
y = (screen_height/2) - (650/2)
window.geometry(f'{1300}x{650}+{int(x)}+{int(y)}')
window.geometry("1300x650")
window.configure(bg="#FFFFFF")
window.title(name)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=650,
    width=1300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    650.0,
    325.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    650.0,
    325.0,
    image=image_image_2
)

canvas.create_text(
    388.0,
    56.0,
    anchor="nw",
    text="Сопутствующие заболевания (отметить):",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    97.0,
    108.0,
    anchor="nw",
    text="A. Гипертоническая болезнь",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var1 = IntVar()
Checkbutton(window, variable=var1).place(x=65, y=105)

canvas.create_text(
    97.0,
    161.0,
    anchor="nw",
    text="B. Ишемическая болезнь сердца. Стабильная стенокардия нарушения",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var2 = IntVar()
Checkbutton(window, variable=var2).place(x=65, y=158)

canvas.create_text(
    97.0,
    214.0,
    anchor="nw",
    text="C. В анамнезе перенесенный ИМ",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var3 = IntVar()
Checkbutton(window, variable=var3).place(x=65, y=211)

canvas.create_text(
    97.0,
    267.0,
    anchor="nw",
    text="D. В анамнезе перенесенный ОНМК, ТИА",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var4 = IntVar()
Checkbutton(window, variable=var4).place(x=65, y=264)

canvas.create_text(
    97.0,
    320.0,
    anchor="nw",
    text="E. ХСН",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var5 = IntVar()
Checkbutton(window, variable=var5).place(x=65, y=317)

canvas.create_text(
    97.0,
    373.0,
    anchor="nw",
    text="F. Атеросклероз периферический многососудистый со стенозом \nи/или эндоартерэктомии в анамнезе, аневризма аорты",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var6 = IntVar()
Checkbutton(window, variable=var6).place(x=65, y=370)

canvas.create_text(
    768.0,
    108.0,
    anchor="nw",
    text="G. Перенесенные операции на сердце и сосудах:",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var7 = IntVar()
Checkbutton(window, variable=var7).place(x=737, y=105)

canvas.create_text(
    768.0,
    161.0,
    anchor="nw",
    text="H. H Нарушения ритма:",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var8 = IntVar()
Checkbutton(window, variable=var8).place(x=737, y=158)

canvas.create_text(
    768.0,
    214.0,
    anchor="nw",
    text="I. Сахарный диабет без осложнений",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var9 = IntVar()
Checkbutton(window, variable=var9).place(x=737, y=211)

canvas.create_text(
    768.0,
    267.0,
    anchor="nw",
    text="J. Сахарный диабет с осложнениями",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var10 = IntVar()
Checkbutton(window, variable=var10).place(x=737, y=264)

canvas.create_text(
    768.0,
    320.0,
    anchor="nw",
    text="K. Нарушение толерантности к глюкозе",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var11 = IntVar()
Checkbutton(window, variable=var11).place(x=737, y=317)

canvas.create_text(
    768.0,
    373.0,
    anchor="nw",
    text="L. ХБП",
    fill="#000000",
    font=("Inter", 16 * -1)
)
var12 = IntVar()
Checkbutton(window, variable=var12).place(x=737, y=370)

canvas.create_text(
    95.0,
    461.0,
    anchor="nw",
    text="Употребление алкоголя (отметить):",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    470.0,
    461.0,
    anchor="nw",
    text="да",
    fill="#000000",
    font=("Inter", 16 * -1)
)
smoke = IntVar()
Radiobutton(window, variable=smoke,
            value=1, font=('Helvetica', 11)).place(x=430, y=459)

canvas.create_text(
    564.0,
    461.0,
    anchor="nw",
    text="нет",
    fill="#000000",
    font=("Inter", 16 * -1)
)
Radiobutton(window, variable=smoke,
            value=2, font=('Helvetica', 11)).place(x=524, y=459)

canvas.create_text(
    661.0,
    461.0,
    anchor="nw",
    text="курил в прошлом",
    fill="#000000",
    font=("Inter", 16 * -1)
)
Radiobutton(window, variable=smoke,
            value=3, font=('Helvetica', 11)).place(x=621, y=459)

canvas.create_text(
    116.0,
    540.0,
    anchor="nw",
    text="САД мм.рт.ст",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    495.0,
    540.0,
    anchor="nw",
    text="ДАД мм.рт.ст",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    354.0,
    554.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=305.0,
    y=540.0,
    width=98.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    773.0,
    556.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=724.0,
    y=542.0,
    width=98.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=next1,
    relief="flat"
)
button_1.place(
    x=973.0,
    y=535.0,
    width=194.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()

#          Test3

window2 = Tk()
screen_width = window2.winfo_screenwidth()
screen_height = window2.winfo_screenheight()
x = (screen_width/2) - (1300/2)
y = (screen_height/2) - (450/2)
window2.geometry(f'{1300}x{450}+{int(x)}+{int(y)}')
window2.geometry("1300x450")
window2.configure(bg="#FFFFFF")
window2.title(name)

canvas = Canvas(
    window2,
    bg="#FFFFFF",
    height=450,
    width=1300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    650.0,
    225.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=next2,
    relief="flat"
)
button_1.place(
    x=1016.0,
    y=400.0,
    width=194.0,
    height=41.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("tst2.png"))
image_2 = canvas.create_image(
    649.0,
    224.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("test2e.png"))
entry_bg_1 = canvas.create_image(
    926.5,
    206.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=870.0,
    y=187.0,
    width=113.0,
    height=36.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("test2e.png"))
entry_bg_2 = canvas.create_image(
    926.5,
    253.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=870.0,
    y=234.0,
    width=113.0,
    height=36.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("test2e.png"))
entry_bg_3 = canvas.create_image(
    926.5,
    300.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=870.0,
    y=281.0,
    width=113.0,
    height=36.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("test2e.png"))
entry_bg_4 = canvas.create_image(
    926.5,
    347.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place(
    x=870.0,
    y=328.0,
    width=113.0,
    height=36.0
)
window2.resizable(False, False)
window2.mainloop()

#                 Test END

window3 = Tk()
screen_width = window3.winfo_screenwidth()
screen_height = window3.winfo_screenheight()
x = (screen_width/2) - (1300/2)
y = (screen_height/2) - (450/2)
window3.geometry(f'{1300}x{450}+{int(x)}+{int(y)}')
window3.geometry("1300x450")
window3.configure(bg="#FFFFFF")
window3.title(name)

canvas = Canvas(
    window3,
    bg="#FFFFFF",
    height=450,
    width=1300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    650.0,
    225.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("end.png"))
image_2 = canvas.create_image(
    650.0,
    225.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=result,
    relief="flat"
)
button_1.place(
    x=999.0,
    y=379.0,
    width=194.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_1 = canvas.create_image(
    836.0,
    157.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=783.0,
    y=140.0,
    width=106.0,
    height=33.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_2 = canvas.create_image(
    836.0,
    204.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=783.0,
    y=187.0,
    width=106.0,
    height=33.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    836.0,
    251.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=783.0,
    y=234.0,
    width=106.0,
    height=33.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_4 = canvas.create_image(
    836.0,
    298.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place(
    x=783.0,
    y=281.0,
    width=106.0,
    height=33.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_5 = canvas.create_image(
    836.0,
    345.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_5.place(
    x=783.0,
    y=328.0,
    width=106.0,
    height=33.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_6 = canvas.create_image(
    836.0,
    392.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_6.place(
    x=783.0,
    y=375.0,
    width=106.0,
    height=33.0
)
window3.resizable(False, False)
window3.mainloop()
