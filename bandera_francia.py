#------------------------------
# Bandera Francia
#------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#------------------------------
# funciones de la app
#------------------------------

#------------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Francia")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame azul
#------------------------------
frame_azul= Frame(ventana_principal)
frame_azul.config(bg="dark blue", width=166, height=500)
frame_azul.place(x=0, y=0)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=166, height=500)
frame_blanco.place(x=166, y=0)

#------------------------------
# frame rojo
#------------------------------
frame_rojo= Frame(ventana_principal)
frame_rojo.config(bg="red", width=266, height=600)
frame_rojo.place(x=332, y=0)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()