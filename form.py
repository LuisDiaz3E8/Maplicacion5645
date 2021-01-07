from tkinter import *
from tkinter import ttk
import datetime
import sqlite3



conn = sqlite3.connect('Ciclistaslocos.db')

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



#formulario()
    





