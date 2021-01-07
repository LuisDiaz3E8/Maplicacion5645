from tkinter import *
from tkinter import ttk
import time
import PIL
import sqlite3
import form # importando las varibables y funciones de otro codigo que ya habia hecho
import datetime

tipoSangre = [
    "A+", 
    "A-", 
    "B+", 
    "B-", 
    "O+", 
    "O-", 
    "AB+",
    "AB-",
    "Otros"]

tipoSize = ["S", "M", "L"]

# Base de Datos. Table de los datos de los ciclistas

conn = sqlite3.connect('Ciclistaslocos.db')
tablesCreation = conn.cursor()
# Nota: el nombre de la base de datos simplemente me quede sin ideas ;)
tablesCreation.execute (""" CREATE TABLE IF NOT EXISTS Ciclistas (
   
    cedula INT,
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    Tipo_de_sangre NVARCHAR(100),
    Size_de_bicicleta NVARCHAR(100),
    Size_de_uniforme NVARCHAR(100),
    Telefono NVARCHAR(100),
    Celular NVARCHAR(100),
    Email NVARCHAR(100),
    Direccion NVARCHAR(100),
    Persona_de_contacto NVARCHAR(100),
    Telefono_de_contacto NVARCHAR(100),
    Fecha_de_registro DATETIME 
    
    )""")

conn.commit
conn.close





def hovering(hover):


    menus1.etiqueta1["image"] = menus1.C_gestions_icon_white

def hovering2(hover):

    menus1.etiqueta2["image"] = menus1.a_actividades_white



def unhovering(event):
    menus1.etiqueta1["image"] = menus1.C_gestions_icon

def unhovering2(event):
    menus1.etiqueta2["image"] = menus1.a_actividades_icon


def despliegue1():
    
    

    if menus1.menu_desplegable == False and menus1.animation == 0:
        menus1.menu_desplegable = True

        while menus1.animation < 0.2 :
            menus1.animation += 0.01
            menus1.listadespliege += 0.01
            if round(menus1.animation,2) == 0.19:
                menus1.animation = 0.2
                     
                   
            menus1.frame_3.place(relheight = 1, relwidth = menus1.animation, rely = 0, relx = 0.04)
            menus1.frame_2.place(relheight = 1, relwidth = 1, rely = 0, relx = menus1.listadespliege )
            
            

            menus1.frame_3.update_idletasks()
            menus1.frame_3.update()

            time.sleep(.001)    
            
            


    elif menus1.menu_desplegable == True and menus1.animation == 0.2 :
        menus1.menu_desplegable = False
        
        #animation = 0.2

        while menus1.animation > 0:
            menus1.animation -= 0.01
            menus1.listadespliege -= 0.01
            if round(menus1.animation,2) == 0.01:
                menus1.animation = 0
                
                

            menus1.frame_3.place(relheight = 1, relwidth = menus1.animation, rely = 0, relx = 0.04)
            menus1.frame_2.place(relheight = 1, relwidth = 1, rely = 0, relx = menus1.listadespliege )

                

            menus1.frame_3.update_idletasks()
            menus1.frame_3.update()
            time.sleep(0.001)
            
            


class menus1 ():

    principal = Tk()
    principal.title("Ciclistas S X A")
    principal.geometry("1200x720")
    principal.configure(background = "#503A99")
    animation = 0
    animation1 = 1

    listadespliege = 0.04

    

   


    
    #principal.attributes("-topmost", True)
    
    #color de los botones principal
    buttonColor = "#503A99"

    botonesSec = "#3B2A73"

    menu_desplegable = False

    despliegue = 0

    C_gestions_icon = PhotoImage(file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\grid32b.PNG")
    C_gestions_icon_white = PhotoImage(file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\grid32.PNG")
    
    reportes = PhotoImage(file =r"D:\Visual Studio Code\Python\Maplicacion5645\icons\bar-chart.PNG")

    about = PhotoImage(file = r"D:\Visual Studio Code\Python\Maplicacion5645\icons\about.PNG")

    salida = PhotoImage(file = r"D:\Visual Studio Code\Python\Maplicacion5645\icons\salida.PNG")


    a_actividades_icon = PhotoImage (file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\archive32.PNG")
    a_actividades_white = PhotoImage (file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\archive32W.PNG")

    frame_1 = Frame(principal, bg="#503A99")
    frame_2 = Frame(principal, bg="#281C4D")
    frame_3 = Frame(principal, bg= "#3B2A73")

    etiqueta1 = Button(frame_1, text= "Gestionar ciclista", bg = buttonColor, image = C_gestions_icon, command = despliegue1, relief = FLAT )
    etiqueta2 = Button(frame_1, text= "Gestionar Actividades",bg = buttonColor, image = a_actividades_icon, relief = FLAT )
    etiqueta3 = Button(frame_1, text= "Reporte",bg = buttonColor, image = reportes, relief = FLAT)
    etiqueta4 = Button(frame_1, text= "Acerca de",bg = buttonColor, image = about, relief = FLAT)
    etiqueta5 = Button(frame_1, text= "Salir",bg = buttonColor, image = salida, relief = FLAT)


    subMenu = Button(frame_3, text ="Ver listado de ciclistas", bg= botonesSec, relief = FLAT, )
    subMenu2 = Button(frame_3, text = "Agregar Ciclistas", bg = botonesSec, relief = FLAT, command = form.formulario)
    subMenu3 = Button(frame_3, text = "Editar Ciclistas", bg = botonesSec, relief = FLAT)
    subMenu4 = Button(frame_3, text = "Eliminar Ciclistas", bg = botonesSec, relief = FLAT)

    

class treeview ():

    columnas= ["Cedula",
        "Nombre", 
        "Apellido",
        "Tipo de Sangre",
        "Size de bicicleta",
        "Size de uniforme",
        "Telefono",
        "Celular",
        "Email",
        "Direccion",
        "Persona de contacto",
        "Telefono de contacto",
        "Fecha de registro"]

    listado_de_ciclistas= ttk.Treeview(menus1.frame_2, columns=(columnas))
    listado_de_ciclistas.pack()

    





def menu_update():
    

    menus1.frame_1.place(relheight = 1, relwidth = 0.04, rely = 0, relx = 0)

    menus1.frame_2.place(relheight = 1, relwidth = 1, rely = 0, relx = menus1.listadespliege)
    
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

    # Muestra el listado de los ciclistas
    treeview.listado_de_ciclistas.place(relheight= 0.5, relwidth = 0.9)
    
    for row in treeview.columnas:
        treeview.listado_de_ciclistas.column(row, minwidth =150)
        treeview.listado_de_ciclistas.heading(row, text= row)
        
    
    




    

    

    menus1.principal.mainloop()






 
menu_update()









def formulario():

    
    formulario = Tk()
    formulario.title ("Formulario")
    formulario.geometry("400x700")
    formulario.configure(background = "#503A99")

    


    

    cedula1 = Label(formulario, text = "Cedula", bg= "#503A99")
    cedula1.pack()
    cedula1.place(rely = 0.065, relx = 0.1)

    cedula = Entry (formulario, width = 50)
    cedula.pack()
    cedula.place (rely = 0.1, relx = 0.1)
    #________________________________________
    nombre1 = Label(formulario, text= "Nombre", bg= "#503A99")
    nombre1.pack()
    nombre1.place(rely= 0.14, relx= 0.1)

    nombre = Entry (formulario, width = 50)
    nombre.pack()
    nombre.place (rely = 0.17, relx = 0.1)
    #____________________________________________
    apellido1 = Label(formulario, text= "Apellido", bg= "#503A99")
    apellido1.pack()
    apellido1.place(rely= 0.21, relx= 0.1)

    apellido = Entry (formulario, width = 50)
    apellido.pack()
    apellido.place (rely = 0.24, relx = 0.1)
    #__________________________________________
    telefono1 = Label(formulario, text= "Telefono", bg="#503A99")
    telefono1.pack()
    telefono1.place(rely= 0.28, relx= 0.1)

    telefono = Entry (formulario, width = 50)
    telefono.pack()
    telefono.place (rely = 0.31, relx = 0.1)
    #_________________________________________
    celular1 = Label(formulario, text= "Celular", bg="#503A99")
    celular1.pack
    celular1.place(rely= 0.35, relx= 0.1)

    celular = Entry(formulario, width=50)
    celular.pack()
    celular.place(rely=0.38, relx= 0.1)
    #___________________________________________
    tipoS1 = Label (formulario, text= "Tipo de sangre", bg="#503A99")
    tipoS1.pack()
    tipoS1.place(rely=0.42, relx= 0.1)

    tipoS = ttk.Combobox(formulario, values= tipoSangre, width = 10, state= "readonly")
    tipoS.set("Seleccione")
    tipoS.pack()
    tipoS.place(rely= 0.45, relx=0.1)
    #___________________________________________
    SizeU1 = Label (formulario, text= "Uniforme Size", bg="#503A99")
    SizeU1.pack()
    SizeU1.place(rely=0.42, relx= 0.4)

    SizeU = ttk.Combobox(formulario, values= tipoSize, width = 10, state= "readonly")
    SizeU.set("Seleccione")
    SizeU.pack()
    SizeU.place(rely= 0.45, relx=0.4)
    #____________________________________________
    SizeB1 = Label (formulario, text= "Bicicleta Size", bg="#503A99")
    SizeB1.pack()
    SizeB1.place(rely=0.42, relx= 0.7)

    SizeB = ttk.Combobox(formulario, values= tipoSize, width = 10, state= "readonly")
    SizeB.set("Seleccione")
    SizeB.pack()
    SizeB.place(rely= 0.45, relx=0.7)

    #________________________________________

    email1 = Label(formulario, text= "Email", bg="#503A99")
    email1.pack()
    email1.place(rely= 0.50, relx= 0.1)
    
    email = Entry(formulario, width= 50)
    email.pack()
    email.place(rely=0.53 , relx=0.1)
    #__________________________________________

    direccion1 = Label(formulario, text= "Dirección", bg="#503A99")
    direccion1.pack()
    direccion1.place(rely= 0.57, relx= 0.1)

    direccion = Entry(formulario, width = 50)
    direccion.pack()
    direccion.place(rely= 0.60, relx= 0.1)
    
    #__________________________________________

    contactop1 = Label(formulario, text= "Persona de contacto", bg="#503A99")
    contactop1.pack()
    contactop1.place(rely= 0.64, relx=0.1)

    contactop = Entry(formulario, width = 50)
    contactop.pack()
    contactop.place(rely= 0.67, relx= 0.1)

    #_________________________________________

    ncontacto1 = Label(formulario, text=  "Numero de contacto", bg="#503A99")
    ncontacto1.pack()
    ncontacto1.place(rely= 0.71, relx=0.1)

    ncontacto = Entry(formulario, width=50)
    ncontacto.pack()
    ncontacto.place(rely=0.74, relx =0.1)
    
    

    

    def testing():
        getCedula= cedula.get()
        getNombre = nombre.get()
        getApellido = apellido.get()
        getTelefono = telefono.get()
        getCelular  = celular.get()
        getTipo_Sangre = tipoS.get()
        getSize_uniforme = SizeU.get()
        getSize_bicicleta   = SizeB.get()
        getEmail    = email.get()
        getDireccion = direccion.get()
        getContacto = contactop.get()
        getN_contacto   = ncontacto.get()
        fechaDe_registro = datetime.date.today()


        # Valores = [
        #     getCedula, 
        #     getNombre, 
        #     getApellido, 
        #     getTelefono, getCelular, 
        #     getTipo_Sangre, 
        #     getSize_uniforme, 
        #     getSize_bicicleta, 
        #     getEmail, 
        #     getDireccion ,
        #     getContacto, 
        #     getN_contacto
        #     ]

        tabla_introducion = conn.cursor()
        
        # los signos de interrogacion son placeholders dicho en español estan ahi hasta que se le assigne un valor
        sql = """INSERT INTO Ciclistas(
            cedula, 
            nombre, 
            apellido, 
            Tipo_de_sangre, 
            Size_de_bicicleta, 
            Size_de_uniforme, 
            Telefono, 
            Celular, 
            Email, 
            Direccion,
            Persona_de_contacto,
            Telefono_de_contacto,
            Fecha_de_registro) 
             
             Values (?, ?, ?, ?, ?, ? , ?, ? , ?, ?, ? ,?, ?)"""
        tabla_introducion.execute(sql, (
            getCedula,
            getNombre, 
            getApellido, 
            getTipo_Sangre,  
            getSize_bicicleta,  
            getSize_uniforme, 
            getTelefono,
            getCelular,
            getEmail,
            getDireccion,
            getContacto,
            getN_contacto,
            fechaDe_registro
            
            ))

        

        conn.commit() 

        # tabla_introducion.execute("SELECT * FROM Ciclistas")
        # for items in tabla_introducion:
        #     Gui.menus1.listado_de_ciclistas.insert(parent="",index="end", values= items)

        conn.close()
        formulario.destroy()

    def destroy ():
        conn.close()
        formulario.destroy()
        

    Agregar = Button (formulario, text= "Agregar", command= testing)
    Agregar.place(rely= 0.9 , relx =0.4)

    cancelar1 = Button (formulario, text= "cancelar", command= destroy)
    cancelar1.place(rely= 0.9 , relx =0.8)

    

    
    formulario.mainloop()









