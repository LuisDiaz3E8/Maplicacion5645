from tkinter import *

def formulario():
    formulario = Tk()
    formulario.title ("Formulario")
    formulario.geometry("400x700")
    formulario.configure(background = "#503A99")


    Cedula = Entry (formulario, width = 50)
    Cedula.pack()
    Cedula.place (rely = 0.1, relx = 0.1)


    nombre = Entry (formulario, width = 50)
    nombre.pack()
    nombre.place (rely = 0.2, relx = 0.1)

    apellido = Entry (formulario, width = 50)
    apellido.pack()
    apellido.place (rely = 0.3, relx = 0.1)

    fechaN = Entry (formulario, width = 50)
    fechaN.pack()
    fechaN.place (rely = 0.4, relx = 0.1)

    

    




    formulario.mainloop()



formulario()

