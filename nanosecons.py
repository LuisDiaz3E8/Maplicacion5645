import time
from tkinter import *


class menu1():
    ver = 0
    main = Tk()
    marco = Frame(main, bg= "black")

    mennu_desplegable = False





def menu_principal():




    
    
    class menus ():
        
        menu1.main.geometry("1200x720")
        


        
        menu1.marco.place(relheight = 1, relwidth = menu1.ver, rely = 0, relx = 0)
       
        boton = Button(menu1.main, bg= "black", padx = 30 , pady = 30, command = probando )
        boton.pack

        boton2 = Button(menu1.main, bg= "black", padx = 30 , pady = 30, command = probando2 )
        boton2.pack(side = BOTTOM)

        
        boton.pack(side = RIGHT)



        


        menu1.marco.mainloop()
    

    

def probando():
    animation = 0
    

    if menu1.mennu_desplegable == False:
        menu1.mennu_desplegable = True
        
        while animation <= 0.2:
            
            
            animation += 0.01
            menu1.marco.place(relheight = 1, relwidth = animation, rely = 0, relx = 0)

                        
            
            time.sleep(.001)
            menu1.marco.update_idletasks()
            menu1.marco.update()
        
    mennu_desplegable = True
            
            
def probando2():
    animation = 0.2
    

    if menu1.mennu_desplegable == True:
        menu1.mennu_desplegable = False
        while animation >= 0:
            
            
            
            menu1.marco.place(relheight = 1, relwidth = animation, rely = 0, relx = 0)
            animation -= 0.01

                        
            
            time.sleep(.001)
            menu1.marco.update_idletasks()
            menu1.marco.update()
    

    
            


menu_principal()




    


