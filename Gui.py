from tkinter import *
import time
import PIL
import sqlite3




class ciclistas:
    pass



class Actividades:
    pass

def hovering(hover):


    menus1.etiqueta1["image"] = menus1.C_gestions_icon_white

def hovering2(hover):

    menus1.etiqueta2["image"] = menus1.a_actividades_white



def unhovering(event):
    menus1.etiqueta1["image"] = menus1.C_gestions_icon

def unhovering2(event):
    menus1.etiqueta2["image"] = menus1.a_actividades_icon


def despliegue1():
    animation = 0
    

    if menus1.menu_desplegable == False:
        menus1.menu_desplegable = True

        while animation < 0.2 :

            if round(animation,2) == 0.19:
                animation = 0.2     
                   
            menus1.frame_3.place(relheight = 1, relwidth = animation, rely = 0, relx = 0.04)
            animation += 0.01

            menus1.frame_3.update_idletasks()
            menus1.frame_3.update()

            time.sleep(.001)    
            
            


    elif menus1.menu_desplegable == True:
        menus1.menu_desplegable = False
        
        animation = 0.2

        while animation > 0:

            if round(animation,2) == 0.01:
                animation = 0
                

            menus1.frame_3.place(relheight = 1, relwidth = animation, rely = 0, relx = 0.04)
            animation -= 0.01
                

            menus1.frame_3.update_idletasks()
            menus1.frame_3.update()
            time.sleep(0.001)
            
            


class menus1 ():

    principal = Tk()
    principal.title("Ciclistas S X A")
    principal.geometry("1200x720")
    principal.configure(background = "#503A99")


    principal.overrideredirect(True) # turns off title bar, geometry
    #principal.geometry('400x100+200+200') # set new geometry

    # make a frame for the title bar
    title_bar = Frame(principal, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

    # put a close button on the title bar
    close_button = Button(title_bar, text='X', command=principal.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)

    # a canvas for the main area of the window
    window = Canvas(principal, bg='#2e2e2e',highlightthickness=0)

    title_bar.pack(expand=1, fill=X)
    close_button.pack(side=RIGHT)
    window.pack(expand=1, fill=BOTH)
    xwin=None
    ywin=None


    
    #principal.attributes("-topmost", True)
    
    #color de los botones principal
    buttonColor = "#503A99"

    botonesSec = "#3B2A73"

    menu_desplegable = False

    despliegue = 0

    C_gestions_icon = PhotoImage(file=r"D:\Visual Studio Code\Python\icons\grid32b.PNG")
    C_gestions_icon_white = PhotoImage(file=r"D:\Visual Studio Code\Python\icons\grid32.PNG")
    
    reportes = PhotoImage(file =r"D:\Visual Studio Code\Python\icons\bar-chart.PNG")

    about = PhotoImage(file = r"D:\Visual Studio Code\Python\icons\about.PNG")

    salida = PhotoImage(file = r"D:\Visual Studio Code\Python\icons\salida.PNG")


    a_actividades_icon = PhotoImage (file=r"D:\Visual Studio Code\Python\icons\archive32.PNG")
    a_actividades_white = PhotoImage (file=r"D:\Visual Studio Code\Python\icons\archive32W.PNG")

    frame_1 = Frame(principal, bg="#503A99")
    frame_2 = Frame(principal, bg="#281C4D")
    frame_3 = Frame(principal, bg= "#3B2A73")

    etiqueta1 = Button(frame_1, text= "Gestionar ciclista", bg = buttonColor, image = C_gestions_icon, command = despliegue1, relief = FLAT )
    etiqueta2 = Button(frame_1, text= "Gestionar Actividades",bg = buttonColor, image = a_actividades_icon, relief = FLAT )
    etiqueta3 = Button(frame_1, text= "Reporte",bg = buttonColor, image = reportes, relief = FLAT)
    etiqueta4 = Button(frame_1, text= "Acerca de",bg = buttonColor, image = about, relief = FLAT)
    etiqueta5 = Button(frame_1, text= "Salir",bg = buttonColor, image = salida, relief = FLAT)


    subMenu = Button(frame_3, text ="Ver listado de ciclistas", bg= botonesSec, relief = FLAT)
    subMenu2 = Button(frame_3, text = "Agregar Ciclistas", bg = botonesSec, relief = FLAT)
    subMenu3 = Button(frame_3, text = "Editar Ciclistas", bg = botonesSec, relief = FLAT)
    subMenu4 = Button(frame_3, text = "Eliminar Ciclistas", bg = botonesSec, relief = FLAT)





def menu_update():

    menus1.frame_1.place(relheight = 1, relwidth = 0.04, rely = 0, relx = 0)

    menus1.frame_2.place(relheight = 1, relwidth = 1, rely = 0, relx = 0.04)
    
    # Frame del menu desplegable

    menus1.frame_3.place(relheight = 1, relwidth = menus1.despliegue, rely = 0, relx = 0.04)

    # ajustes de Menu Principal
    menus1.etiqueta1.place( rely = 0.1, relx = 0.1)
    menus1.etiqueta2.place( rely = 0.2, relx = 0.1)
    menus1.etiqueta3.place( rely = 0.3, relx = 0.1)
    menus1.etiqueta4.place( rely = 0.4, relx = 0.1)
    menus1.etiqueta5.place( rely = 0.5, relx = 0.1)
    
    # ajustes de sub-menu de ciclistas
    menus1.subMenu.place(rely = 0.1, relx = 0.1)
    menus1.subMenu2.place(rely = 0.2, relx = 0.1)
    menus1.subMenu3.place(rely = 0.3, relx = 0.1)
    menus1.subMenu4.place(rely = 0.4, relx = 0.1)
    
    menus1.etiqueta1.bind("<Enter>", hovering)
    menus1.etiqueta1.bind("<Leave>", unhovering)
    menus1.etiqueta2.bind("<Enter>", hovering2)
    menus1.etiqueta2.bind("<Leave>", unhovering2)

    menus1.principal.mainloop()







            

            






















menu_update()













