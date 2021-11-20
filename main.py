from tkinter import *

def ekran(item):
    """Ekranga chiqazadi"""
    tmp = str(text_input.get())
    text_input.set(tmp + item)

def clear():
    """C bosilganda ochirib beradi"""
    text_input.set('')

def hisobla():
    """Amallarni hisoblaydi"""
    tmp = str(text_input.get())
    s = eval(tmp)
    text_input.set(s)

def ortga_ochirish(item):
    """Ortga ochirish"""
    ochir = str(text_input.get())
    ochir = ochir[:-1]
    text_input.set(ochir)


oyna = Tk()
text_input = StringVar()
oyna.title("Kalkulyator")
entry = Entry(oyna, font = {'arial', 20, 'bold'}, width = 27, textvariable = text_input, bg = 'silver', bd = 20, justify = 'right').grid(row = 0, columnspan = 5)

tugma_c = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = 'C', fg = 'black', bg = 'red', bd = 10,command = lambda : clear()).grid(row = 1, column = 0)
tugma_foiz = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '%', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('%') ).grid(row = 1, column = 1)
tugma_och = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '<', fg = 'black', bg = 'Cyan', bd = 10, command = lambda : ortga_ochirish('<')).grid(row = 1, column = 2)
bolish = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '/', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('/') ).grid(row = 1, column = 3)

tugma7 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '7', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('7')).grid(row = 2, column = 0)
tugma8 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '8', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('8') ).grid(row = 2, column = 1)
tugma9 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '9', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('9') ).grid(row = 2, column = 2)
kopaytr = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '*', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('*') ).grid(row = 2, column = 3)

tugma4 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '4', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('4') ).grid(row = 3, column = 0)
tugma5 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '5', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('5') ).grid(row = 3, column = 1)
tugma6 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '6', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('6') ).grid(row = 3, column = 2)
minus = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '-', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('-') ).grid(row = 3, column = 3)

tugma1 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '1', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('1') ).grid(row = 4, column = 0)
tugma2 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '2', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('2') ).grid(row = 4, column = 1)
tugma3 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '3', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('3') ).grid(row = 4, column = 2)
qoshish = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '+', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('+') ).grid(row = 4, column = 3)

tugma11 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '()', fg = 'black', bg = '#FF7F50', bd = 10, ).grid(row = 5, column = 0)
tugma0 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '0', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('0') ).grid(row = 5, column = 1)
tugma00 = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '.', fg = 'black', bg = '#FF7F50', bd = 10, command = lambda : ekran('.') ).grid(row = 5, column = 2)
teng = Button(oyna, font = {'arial', 20, 'bold'}, padx = 20, text = '=', fg = 'black', bg = 'green', bd = 10, command = lambda : hisobla() ).grid(row = 5, column = 3)

oyna.mainloop()


